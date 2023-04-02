/**********************************************************************************************************/
/***** AUTOGENERATED from git@github.deere.com:Construction-BatteryElectricVehicle/ExternalMaster.git *****/
/**********************************************************************************************************/

#include "StdCANHashValue.h
#include "ExternalMaster_Callbacks.h"


/* Recall that Relevancy_Table_Item struct has members:
*		- UInt8_T relevancy_val
*		- UInt16_T intended_id
*		- void (* cb)(struct Std_CAN_Queeu_Item_S * item)
*		- UInt8_T pack_index */

const struct Relevancy_Table_Item RELEVANCY_HASH_TABLE[STD_QUEUE_HASH_NUM] = 
{
	{	0,		0   ,		NULL,		0 	},
	{	0,		0   ,		NULL,		0 	},
	{	0,		0   ,		NULL,		0 	},
	{	0,		0   ,		NULL,		0 	},
	{	True,		288 ,		VoltStatsBlock_CellVoltage_Callback,		0 	},
	{	True,		289 ,		VoltStatsBlock_CellVoltage_Callback,		1 	},
	{	True,		290 ,		VoltStatsBlock_CellVoltage_Callback,		2 	},
	{	0,		0   ,		NULL,		0 	},
	{	True,		576 ,		TempCoolantOut_Callback,		0 	},
	{	True,		577 ,		TempCoolantOut_Callback,		1 	},
	{	True,		578 ,		TempCoolantOut_Callback,		2 	},
	{	True,		224 ,		Protections_BMSFaults_Callback,		0 	},
	{	True,		225 ,		Protections_BMSFaults_Callback,		1 	},
	{	True,		226 ,		Protections_BMSFaults_Callback,		2 	},
	{	0,		0   ,		NULL,		0 	},
	{	0,		0   ,		NULL,		0 	},
	{	0,		0   ,		NULL,		0 	},
	{	0,		0   ,		NULL,		0 	},
	{	True,		160 ,		Status_BMSContactorState_Callback,		0 	},
	{	True,		161 ,		Status_BMSContactorState_Callback,		1 	},
	{	True,		162 ,		Status_BMSContactorState_Callback,		2 	},
	{	0,		0   ,		NULL,		0 	},
	{	True,		448 ,		IsolationStatus_Callback,		0 	},
	{	True,		449 ,		IsolationStatus_Callback,		1 	},
	{	True,		450 ,		IsolationStatus_Callback,		2 	},
	{	0,		0   ,		NULL,		0 	},
	{	0,		0   ,		NULL,		0 	},
	{	0,		0   ,		NULL,		0 	},
	{	0,		0   ,		NULL,		0 	},
	{	0,		0   ,		NULL,		0 	},
	{	0,		0   ,		NULL,		0 	},
	{	0,		0   ,		NULL,		0 	},
	{	0,		0   ,		NULL,		0 	},
	{	0,		0   ,		NULL,		0 	},
	{	0,		0   ,		NULL,		0 	},
	{	0,		0   ,		NULL,		0 	},
	{	0,		0   ,		NULL,		0 	},
	{	0,		0   ,		NULL,		0 	},
	{	0,		0   ,		NULL,		0 	},
	{	0,		0   ,		NULL,		0 	},
	{	True,		608 ,		TempCell_CellTemp_Callback,		0 	},
	{	True,		609 ,		TempCell_CellTemp_Callback,		1 	},
	{	True,		610 ,		TempCell_CellTemp_Callback,		2 	},
	{	0,		0   ,		NULL,		0 	},
	{	True,		896 ,		StateOfEnergy_SOC_Callback,		0 	},
	{	True,		897 ,		StateOfEnergy_SOC_Callback,		1 	},
	{	True,		898 ,		StateOfEnergy_SOC_Callback,		2 	},
	{	True,		544 ,		TempCoolantIn_Callback,		0 	},
	{	True,		545 ,		TempCoolantIn_Callback,		1 	},
	{	True,		546 ,		TempCoolantIn_Callback,		2 	},
	{	True,		192 ,		Protections_BMSFaults_Callback,		0 	},
	{	True,		193 ,		Protections_BMSFaults_Callback,		1 	},
	{	True,		194 ,		Protections_BMSFaults_Callback,		2 	},
	{	0,		0   ,		NULL,		0 	},
	{	0,		0   ,		NULL,		0 	},
	{	0,		0   ,		NULL,		0 	},
	{	0,		0   ,		NULL,		0 	},
	{	True,		128 ,		Vitals_PackVoltageCurrent_Callback,		0 	},
	{	True,		129 ,		Vitals_PackVoltageCurrent_Callback,		1 	},
	{	True,		130 ,		Vitals_PackVoltageCurrent_Callback,		2 	},
	{	0,		0   ,		NULL,		0 	},
	{	0,		0   ,		NULL,		0 	},
	{	0,		0   ,		NULL,		0 	},
	{	0,		0   ,		NULL,		0 	},
	{	0,		0   ,		NULL,		0 	},
	{	True,		704 ,		StressEst_Callback,		0 	},
	{	True,		705 ,		StressEst_Callback,		1 	},
	{	True,		706 ,		StressEst_Callback,		2 	},
	{	True,		352 ,		PowerLimits_MaxChgDschgCurr_Callback,		0 	},
	{	True,		353 ,		PowerLimits_MaxChgDschgCurr_Callback,		1 	},
	{	True,		354 ,		PowerLimits_MaxChgDschgCurr_Callback,		2 	},

};