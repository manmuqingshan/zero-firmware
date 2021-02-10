#include "bcb.h"
#include "bcb_msmnt.h"
#include "bcb_ocp_otp.h"
#include "bcb_zd.h"
#include <stdlib.h>
#include <zephyr.h>
#include <device.h>
#include <shell/shell.h>
#include <shell/shell_uart.h>

#define LOG_LEVEL LOG_LEVEL_DBG
#include <logging/log.h>
LOG_MODULE_REGISTER(bcb_shell);

struct bcb_shell_data {
	struct bcb_ocp_test_callback ocp_test_callback;
};

static struct bcb_shell_data shell_data;

static int cmd_open_params(const struct shell *shell, size_t argc, char **argv)
{
	ARG_UNUSED(argc);
	ARG_UNUSED(argv);

	bcb_open();
	return 0;
}

static int cmd_close_params(const struct shell *shell, size_t argc, char **argv)
{
	ARG_UNUSED(argc);
	ARG_UNUSED(argv);

	bcb_close();
	return 0;
}

static int cmd_ocp_trigger_params(const struct shell *shell, size_t argc, char **argv)
{
	int direction = BCB_OCP_DIRECTION_P;
	if (argc > 1) {
		switch ((int)argv[1][0]) {
		case 'p':
		case 'P':
			direction = BCB_OCP_DIRECTION_P;
			break;
		case 'n':
		case 'N':
			direction = BCB_OCP_DIRECTION_N;
			break;
		default:
			direction = BCB_OCP_DIRECTION_P;
		}
	} else {
		direction = BCB_OCP_DIRECTION_P;
	}

	bcb_ocp_test_trigger(direction, true);
	return 0;
}

static int cmd_temp_params(const struct shell *shell, size_t argc, char **argv)
{
	if (argc != 2) {
		shell_print(shell, "Invalid sensor");
		shell_print(shell, "Available sensors:");
		shell_print(shell, "    %d: PWR_IN", BCB_TEMP_SENSOR_PWR_IN);
		shell_print(shell, "    %d: PWR_OUT", BCB_TEMP_SENSOR_PWR_OUT);
		shell_print(shell, "    %d: AMB", BCB_TEMP_SENSOR_AMB);
		shell_print(shell, "    %d: MCU", BCB_TEMP_SENSOR_MCU);
		return -1;
	}
	bcb_temp_sensor_t sensor = (bcb_temp_sensor_t)(argv[1][0] - '0');
	shell_print(shell, "%d C", bcb_msmnt_get_temp(sensor));
	return 0;
}

static int cmd_voltage_params(const struct shell *shell, size_t argc, char **argv)
{
	ARG_UNUSED(argc);
	ARG_UNUSED(argv);

	shell_print(shell, "%" PRId32 " mV", bcb_msmnt_get_voltage());

	return 0;
}

static int cmd_current_params(const struct shell *shell, size_t argc, char **argv)
{
	ARG_UNUSED(argc);
	ARG_UNUSED(argv);

	shell_print(shell, "%" PRId32 " mA", bcb_msmnt_get_current());

	return 0;
}

static int cmd_frequency_params(const struct shell *shell, size_t argc, char **argv)
{
	ARG_UNUSED(argc);
	ARG_UNUSED(argv);

	uint32_t frequency = bcb_zd_get_frequency();
	shell_print(shell, "%" PRIu32 ".%03" PRIu32 " Hz", frequency / 1000, frequency % 1000);

	return 0;
}

static void on_ocp_test_activated(bcb_ocp_direction_t direction, uint32_t duration)
{
	LOG_INF("OCP Test completed: direction %c, duration %" PRIu32 " ns",
		direction == BCB_OCP_DIRECTION_N ? 'N' : 'P', duration);
}

int bcb_shell_init(void)
{
	memset(&shell_data, 0, sizeof(shell_data));
	shell_data.ocp_test_callback.handler = on_ocp_test_activated;

	bcb_ocp_test_add_callback(&shell_data.ocp_test_callback);

	return 0;
}

SHELL_STATIC_SUBCMD_SET_CREATE(breaker_sub, 
			       SHELL_CMD(close, NULL, "Close switch.", cmd_close_params),
			       SHELL_CMD(open, NULL, "Open switch.", cmd_open_params),
			       SHELL_CMD(ocpt, NULL, "Trigger OCP.", cmd_ocp_trigger_params),
			       SHELL_CMD(temp, NULL, "Get temperature.", cmd_temp_params),
			       SHELL_CMD(voltage, NULL, "Get voltage.", cmd_voltage_params),
			       SHELL_CMD(current, NULL, "Get current.", cmd_current_params),
			       SHELL_CMD(frequency, NULL, "Get frequency.", cmd_frequency_params),
			       SHELL_SUBCMD_SET_END /* Array terminated. */
);
SHELL_CMD_REGISTER(breaker, &breaker_sub, "Breaker commands", NULL);
