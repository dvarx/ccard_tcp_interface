# CCARD PC Interface
A repository to implement a TCP connection beteween the TMDSCNCD28388D Control Card and a Windows or Linux / ROS PC.

## Network Configuration

### PC Settings

* Subnet Mask : `255.255.255.0`
* IP : `192.168.0.1`
* Gateway : `192.168.0.0`

### Control Card Settings

The network configuration of the Control Card is done in the `main` routine of the CM at `lwIPInit(0, pucMACArray, IPAddr, NetMask, GWAddr, IPADDR_USE_STATIC);`.

* Subnet Mask : `255.255.255.0`
* IP : `192.168.0.4`

## Compilation & Deploying

* Fork the `ethernet_c28_config` project from the ressource explorer in CCS.

* Compile `ethernet_c28_config` and `enet_lwip`

* Under `Run`->`Debug Configurations`->`Main`->`Target Configuration` select `C28xx_CPU1` and `Cortex_M4_0`, then click `Debug`

* In the Debug Perspective select `Connect Target` for both CPU targets:

  ![](img\connect_target.png)

* Load the compiled codes of the two projects first onto `C28xx_CPU1` and then on `Cortex_M4_0`:

  ![](\img\program_target.png)

