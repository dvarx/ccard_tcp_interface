/*
 * comm_interface.h
 *
 *  Created on: 04.11.2021
 *      Author: spadmin
 */

#ifndef COMM_INTERFACE_H_
#define COMM_INTERFACE_H_


enum command{STOP_ALL=0,BUCK_ENABLE_ALL=1};

#define CMD_LENGTH 4

extern const char CMD_STOP[4];
extern const char ENABLE_ALL_BUCK[4];

#endif /* COMM_INTERFACE_H_ */
