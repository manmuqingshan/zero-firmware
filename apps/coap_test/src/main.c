/*
 * Copyright (c) 2015 Intel Corporation
 *
 * SPDX-License-Identifier: Apache-2.0
 */

#include <zephyr.h>
#include <bcb_coap.h>

#define LOG_LEVEL LOG_LEVEL_INF
#include <logging/log.h>
LOG_MODULE_REGISTER(bcb_coap_app);

void main(void)
{
    LOG_INF("Coap Test Application");
    bcb_coap_start_server();
    do {
        bcb_coap_process();
    } while(1);
    LOG_INF("Coap Test Application Exit");
}