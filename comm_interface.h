/*
 * comm_interface.h
 *
 *  Created on: 04.11.2021
 *      Author: spadmin
 */

#ifndef COMM_INTERFACE_H_
#define COMM_INTERFACE_H_

#include <stdint.h>

enum command{IPC_MSG_STOP_ALL=0,IPC_MSG_NEW_MSG=1};

#define NO_CHANNELS 6


struct tnb_mns_msg{
    int16_t desCurrents[NO_CHANNELS];
    uint16_t desDuties[NO_CHANNELS];
    uint8_t stp_flg_byte;
    uint8_t buck_flg_byte;
    uint8_t regen_flg_byte;
    uint8_t  resen_flg_byte;
};

extern const unsigned int OFFSET_DES_DUTIES;
extern const unsigned int OFFSET_STP_FLG_BYTE;
extern const unsigned int OFFSET_BUCK_FLG_BYTE;
extern const unsigned int OFFSET_REGEN_FLG_BYTE;
extern const unsigned int OFFSET_RESEN_FLG_BYTE;


#endif /* COMM_INTERFACE_H_ */
