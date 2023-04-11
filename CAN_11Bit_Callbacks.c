void Vitals_PackVoltageCurrent_Pack1_Callback(struct Std_CAN_Queue_Item_S * item)
{
	JD_WriteVarValueStatus( CAN_11Bit_Pack1_Voltage, ( (JD_VARMNGR_OBJ)item->data[0] ) | ( ( (JD_VARMNGR_OBJ)item->data[1] ) << 8 ), DATA_GOODDATA );
	JD_WriteVarValueStatus( CAN_11Bit_Pack1_Current, ( (JD_VARMNGR_OBJ)item->data[2] ) | ( ( (JD_VARMNGR_OBJ)item->data[3] ) << 8 ), DATA_GOODDATA );
	JD_WriteVarValueStatus( CAN_11Bit_Pack1_DCBusVoltage, ( (JD_VARMNGR_OBJ)item->data[4] ) | ( ( (JD_VARMNGR_OBJ)item->data[5] ) << 8 ), DATA_GOODDATA );
}

void Vitals_PackVoltageCurrent_Pack2_Callback(struct Std_CAN_Queue_Item_S * item)
{
	JD_WriteVarValueStatus( CAN_11Bit_Pack2_Voltage, ( (JD_VARMNGR_OBJ)item->data[0] ) | ( ( (JD_VARMNGR_OBJ)item->data[1] ) << 8 ), DATA_GOODDATA );
	JD_WriteVarValueStatus( CAN_11Bit_Pack2_Current, ( (JD_VARMNGR_OBJ)item->data[2] ) | ( ( (JD_VARMNGR_OBJ)item->data[3] ) << 8 ), DATA_GOODDATA );
	JD_WriteVarValueStatus( CAN_11Bit_Pack2_DCBusVoltage, ( (JD_VARMNGR_OBJ)item->data[4] ) | ( ( (JD_VARMNGR_OBJ)item->data[5] ) << 8 ), DATA_GOODDATA );
}

void Vitals_PackVoltageCurrent_Pack3_Callback(struct Std_CAN_Queue_Item_S * item)
{
	JD_WriteVarValueStatus( CAN_11Bit_Pack3_Voltage, ( (JD_VARMNGR_OBJ)item->data[0] ) | ( ( (JD_VARMNGR_OBJ)item->data[1] ) << 8 ), DATA_GOODDATA );
	JD_WriteVarValueStatus( CAN_11Bit_Pack3_Current, ( (JD_VARMNGR_OBJ)item->data[2] ) | ( ( (JD_VARMNGR_OBJ)item->data[3] ) << 8 ), DATA_GOODDATA );
	JD_WriteVarValueStatus( CAN_11Bit_Pack3_DCBusVoltage, ( (JD_VARMNGR_OBJ)item->data[4] ) | ( ( (JD_VARMNGR_OBJ)item->data[5] ) << 8 ), DATA_GOODDATA );
}

void Status_BMSContactorState_Pack1_Callback(struct Std_CAN_Queue_Item_S * item)
{
}

void Status_BMSContactorState_Pack2_Callback(struct Std_CAN_Queue_Item_S * item)
{
}

void Status_BMSContactorState_Pack3_Callback(struct Std_CAN_Queue_Item_S * item)
{
}

void StateOfEnergy_SOC_Pack1_Callback(struct Std_CAN_Queue_Item_S * item)
{
}

void StateOfEnergy_SOC_Pack2_Callback(struct Std_CAN_Queue_Item_S * item)
{
}

void StateOfEnergy_SOC_Pack3_Callback(struct Std_CAN_Queue_Item_S * item)
{
}

void PowerLimits_MaxChgDschgCurr_Pack1_Callback(struct Std_CAN_Queue_Item_S * item)
{
	JD_WriteVarValueStatus( CAN_11Bit_Pack1_MaxCurrentDischarge, ( (JD_VARMNGR_OBJ)item->data[0] ) | ( ( (JD_VARMNGR_OBJ)item->data[1] ) << 8 ), DATA_GOODDATA );
	JD_WriteVarValueStatus( CAN_11Bit_Pack1_MaxCurrentCharge, ( (JD_VARMNGR_OBJ)item->data[2] ) | ( ( (JD_VARMNGR_OBJ)item->data[3] ) << 8 ), DATA_GOODDATA );
}

void PowerLimits_MaxChgDschgCurr_Pack2_Callback(struct Std_CAN_Queue_Item_S * item)
{
	JD_WriteVarValueStatus( CAN_11Bit_Pack2_MaxCurrentDischarge, ( (JD_VARMNGR_OBJ)item->data[0] ) | ( ( (JD_VARMNGR_OBJ)item->data[1] ) << 8 ), DATA_GOODDATA );
	JD_WriteVarValueStatus( CAN_11Bit_Pack2_MaxCurrentCharge, ( (JD_VARMNGR_OBJ)item->data[2] ) | ( ( (JD_VARMNGR_OBJ)item->data[3] ) << 8 ), DATA_GOODDATA );
}

void PowerLimits_MaxChgDschgCurr_Pack3_Callback(struct Std_CAN_Queue_Item_S * item)
{
	JD_WriteVarValueStatus( CAN_11Bit_Pack3_MaxCurrentDischarge, ( (JD_VARMNGR_OBJ)item->data[0] ) | ( ( (JD_VARMNGR_OBJ)item->data[1] ) << 8 ), DATA_GOODDATA );
	JD_WriteVarValueStatus( CAN_11Bit_Pack3_MaxCurrentCharge, ( (JD_VARMNGR_OBJ)item->data[2] ) | ( ( (JD_VARMNGR_OBJ)item->data[3] ) << 8 ), DATA_GOODDATA );
}

void VoltStatsBlock_CellVoltage_Pack1_Callback(struct Std_CAN_Queue_Item_S * item)
{
	JD_WriteVarValueStatus( CAN_11Bit_Pack1_MinCellVoltage, ( (JD_VARMNGR_OBJ)item->data[0] ) | ( ( (JD_VARMNGR_OBJ)item->data[1] ) << 8 ), DATA_GOODDATA );
	JD_WriteVarValueStatus( CAN_11Bit_Pack1_MaxCellVoltage, ( (JD_VARMNGR_OBJ)item->data[2] ) | ( ( (JD_VARMNGR_OBJ)item->data[3] ) << 8 ), DATA_GOODDATA );
}

void VoltStatsBlock_CellVoltage_Pack2_Callback(struct Std_CAN_Queue_Item_S * item)
{
	JD_WriteVarValueStatus( CAN_11Bit_Pack2_MinCellVoltage, ( (JD_VARMNGR_OBJ)item->data[0] ) | ( ( (JD_VARMNGR_OBJ)item->data[1] ) << 8 ), DATA_GOODDATA );
	JD_WriteVarValueStatus( CAN_11Bit_Pack2_MaxCellVoltage, ( (JD_VARMNGR_OBJ)item->data[2] ) | ( ( (JD_VARMNGR_OBJ)item->data[3] ) << 8 ), DATA_GOODDATA );
}

void VoltStatsBlock_CellVoltage_Pack3_Callback(struct Std_CAN_Queue_Item_S * item)
{
	JD_WriteVarValueStatus( CAN_11Bit_Pack3_MinCellVoltage, ( (JD_VARMNGR_OBJ)item->data[0] ) | ( ( (JD_VARMNGR_OBJ)item->data[1] ) << 8 ), DATA_GOODDATA );
	JD_WriteVarValueStatus( CAN_11Bit_Pack3_MaxCellVoltage, ( (JD_VARMNGR_OBJ)item->data[2] ) | ( ( (JD_VARMNGR_OBJ)item->data[3] ) << 8 ), DATA_GOODDATA );
}

void TempCell_CellTemp_Pack1_Callback(struct Std_CAN_Queue_Item_S * item)
{
	JD_WriteVarValueStatus( CAN_11Bit_Pack1_MinCellTemp, ( (JD_VARMNGR_OBJ)item->data[0] ) | ( ( (JD_VARMNGR_OBJ)item->data[1] ) << 8 ), DATA_GOODDATA );
	JD_WriteVarValueStatus( CAN_11Bit_Pack1_MaxCellTemp, ( (JD_VARMNGR_OBJ)item->data[2] ) | ( ( (JD_VARMNGR_OBJ)item->data[3] ) << 8 ), DATA_GOODDATA );
	JD_WriteVarValueStatus( CAN_11Bit_Pack1_AvgCellTemp, ( (JD_VARMNGR_OBJ)item->data[4] ) | ( ( (JD_VARMNGR_OBJ)item->data[5] ) << 8 ), DATA_GOODDATA );
}

void TempCell_CellTemp_Pack2_Callback(struct Std_CAN_Queue_Item_S * item)
{
	JD_WriteVarValueStatus( CAN_11Bit_Pack2_MinCellTemp, ( (JD_VARMNGR_OBJ)item->data[0] ) | ( ( (JD_VARMNGR_OBJ)item->data[1] ) << 8 ), DATA_GOODDATA );
	JD_WriteVarValueStatus( CAN_11Bit_Pack2_MaxCellTemp, ( (JD_VARMNGR_OBJ)item->data[2] ) | ( ( (JD_VARMNGR_OBJ)item->data[3] ) << 8 ), DATA_GOODDATA );
	JD_WriteVarValueStatus( CAN_11Bit_Pack2_AvgCellTemp, ( (JD_VARMNGR_OBJ)item->data[4] ) | ( ( (JD_VARMNGR_OBJ)item->data[5] ) << 8 ), DATA_GOODDATA );
}

void TempCell_CellTemp_Pack3_Callback(struct Std_CAN_Queue_Item_S * item)
{
	JD_WriteVarValueStatus( CAN_11Bit_Pack3_MinCellTemp, ( (JD_VARMNGR_OBJ)item->data[0] ) | ( ( (JD_VARMNGR_OBJ)item->data[1] ) << 8 ), DATA_GOODDATA );
	JD_WriteVarValueStatus( CAN_11Bit_Pack3_MaxCellTemp, ( (JD_VARMNGR_OBJ)item->data[2] ) | ( ( (JD_VARMNGR_OBJ)item->data[3] ) << 8 ), DATA_GOODDATA );
	JD_WriteVarValueStatus( CAN_11Bit_Pack3_AvgCellTemp, ( (JD_VARMNGR_OBJ)item->data[4] ) | ( ( (JD_VARMNGR_OBJ)item->data[5] ) << 8 ), DATA_GOODDATA );
}

void StressEst_Pack1_Callback(struct Std_CAN_Queue_Item_S * item)
{
	JD_WriteVarValueStatus( CAN_11Bit_Pack1_StressEst_Charge, ( (JD_VARMNGR_OBJ)item->data[0] ) | ( ( (JD_VARMNGR_OBJ)item->data[1] ) << 8 ), DATA_GOODDATA );
	JD_WriteVarValueStatus( CAN_11Bit_Pack1_StressEst_Discharge, ( (JD_VARMNGR_OBJ)item->data[2] ) | ( ( (JD_VARMNGR_OBJ)item->data[3] ) << 8 ), DATA_GOODDATA );
}

void StressEst_Pack2_Callback(struct Std_CAN_Queue_Item_S * item)
{
	JD_WriteVarValueStatus( CAN_11Bit_Pack2_StressEst_Charge, ( (JD_VARMNGR_OBJ)item->data[0] ) | ( ( (JD_VARMNGR_OBJ)item->data[1] ) << 8 ), DATA_GOODDATA );
	JD_WriteVarValueStatus( CAN_11Bit_Pack2_StressEst_Discharge, ( (JD_VARMNGR_OBJ)item->data[2] ) | ( ( (JD_VARMNGR_OBJ)item->data[3] ) << 8 ), DATA_GOODDATA );
}

void StressEst_Pack3_Callback(struct Std_CAN_Queue_Item_S * item)
{
	JD_WriteVarValueStatus( CAN_11Bit_Pack3_StressEst_Charge, ( (JD_VARMNGR_OBJ)item->data[0] ) | ( ( (JD_VARMNGR_OBJ)item->data[1] ) << 8 ), DATA_GOODDATA );
	JD_WriteVarValueStatus( CAN_11Bit_Pack3_StressEst_Discharge, ( (JD_VARMNGR_OBJ)item->data[2] ) | ( ( (JD_VARMNGR_OBJ)item->data[3] ) << 8 ), DATA_GOODDATA );
}

void IsolationStatus_Pack1_Callback(struct Std_CAN_Queue_Item_S * item)
{
	JD_WriteVarValueStatus( CAN_11Bit_Pack1_IsolationActive_TF, ( (JD_VARMNGR_OBJ)item->data[6] & 0x01 ), DATA_GOODDATA );
}

void IsolationStatus_Pack2_Callback(struct Std_CAN_Queue_Item_S * item)
{
	JD_WriteVarValueStatus( CAN_11Bit_Pack2_IsolationActive_TF, ( (JD_VARMNGR_OBJ)item->data[6] & 0x01 ), DATA_GOODDATA );
}

void IsolationStatus_Pack3_Callback(struct Std_CAN_Queue_Item_S * item)
{
	JD_WriteVarValueStatus( CAN_11Bit_Pack3_IsolationActive_TF, ( (JD_VARMNGR_OBJ)item->data[6] & 0x01 ), DATA_GOODDATA );
}

void Protections_BMSFaults_Pack1_Callback(struct Std_CAN_Queue_Item_S * item)
{
	JD_WriteVarValueStatus( CAN_11Bit_Pack1_Fault_BatteryCAN, ( (JD_VARMNGR_OBJ)item->data[0] & 0x01 ), DATA_GOODDATA );
	JD_WriteVarValueStatus( CAN_11Bit_Pack1_Fault_Contactor, ( ( (JD_VARMNGR_OBJ)item->data[0] & 0x02 ) >> 1 ), DATA_GOODDATA );
	JD_WriteVarValueStatus( CAN_11Bit_Pack1_Fault_CurrentSensor, ( ( (JD_VARMNGR_OBJ)item->data[0] & 0x04 ) >> 2 ), DATA_GOODDATA );
	JD_WriteVarValueStatus( CAN_11Bit_Pack1_Fault_DCLinkOverVoltage, ( ( (JD_VARMNGR_OBJ)item->data[0] & 0x08 ) >> 3 ), DATA_GOODDATA );
	JD_WriteVarValueStatus( CAN_11Bit_Pack1_Fault_OvercurrentCharge, ( ( (JD_VARMNGR_OBJ)item->data[2] & 0x08 ) >> 3 ), DATA_GOODDATA );
	JD_WriteVarValueStatus( CAN_11Bit_Pack1_Fault_OvercurrentDischarge, ( ( (JD_VARMNGR_OBJ)item->data[2] & 0x20 ) >> 5 ), DATA_GOODDATA );
	JD_WriteVarValueStatus( CAN_11Bit_Pack1_Fault_BatteryCAN, ( ( (JD_VARMNGR_OBJ)item->data[5] & 0x08 ) >> 3 ), DATA_GOODDATA );
}

void Protections_BMSFaults_Pack2_Callback(struct Std_CAN_Queue_Item_S * item)
{
	JD_WriteVarValueStatus( CAN_11Bit_Pack2_Fault_BatteryCAN, ( (JD_VARMNGR_OBJ)item->data[0] & 0x01 ), DATA_GOODDATA );
	JD_WriteVarValueStatus( CAN_11Bit_Pack2_Fault_Contactor, ( ( (JD_VARMNGR_OBJ)item->data[0] & 0x02 ) >> 1 ), DATA_GOODDATA );
	JD_WriteVarValueStatus( CAN_11Bit_Pack2_Fault_CurrentSensor, ( ( (JD_VARMNGR_OBJ)item->data[0] & 0x04 ) >> 2 ), DATA_GOODDATA );
	JD_WriteVarValueStatus( CAN_11Bit_Pack2_Fault_DCLinkOverVoltage, ( ( (JD_VARMNGR_OBJ)item->data[0] & 0x08 ) >> 3 ), DATA_GOODDATA );
	JD_WriteVarValueStatus( CAN_11Bit_Pack2_Fault_OvercurrentCharge, ( ( (JD_VARMNGR_OBJ)item->data[2] & 0x08 ) >> 3 ), DATA_GOODDATA );
	JD_WriteVarValueStatus( CAN_11Bit_Pack2_Fault_OvercurrentDischarge, ( ( (JD_VARMNGR_OBJ)item->data[2] & 0x20 ) >> 5 ), DATA_GOODDATA );
	JD_WriteVarValueStatus( CAN_11Bit_Pack2_Fault_BatteryCAN, ( ( (JD_VARMNGR_OBJ)item->data[5] & 0x08 ) >> 3 ), DATA_GOODDATA );
}

void Protections_BMSFaults_Pack3_Callback(struct Std_CAN_Queue_Item_S * item)
{
	JD_WriteVarValueStatus( CAN_11Bit_Pack3_Fault_BatteryCAN, ( (JD_VARMNGR_OBJ)item->data[0] & 0x01 ), DATA_GOODDATA );
	JD_WriteVarValueStatus( CAN_11Bit_Pack3_Fault_Contactor, ( ( (JD_VARMNGR_OBJ)item->data[0] & 0x02 ) >> 1 ), DATA_GOODDATA );
	JD_WriteVarValueStatus( CAN_11Bit_Pack3_Fault_CurrentSensor, ( ( (JD_VARMNGR_OBJ)item->data[0] & 0x04 ) >> 2 ), DATA_GOODDATA );
	JD_WriteVarValueStatus( CAN_11Bit_Pack3_Fault_DCLinkOverVoltage, ( ( (JD_VARMNGR_OBJ)item->data[0] & 0x08 ) >> 3 ), DATA_GOODDATA );
	JD_WriteVarValueStatus( CAN_11Bit_Pack3_Fault_OvercurrentCharge, ( ( (JD_VARMNGR_OBJ)item->data[2] & 0x08 ) >> 3 ), DATA_GOODDATA );
	JD_WriteVarValueStatus( CAN_11Bit_Pack3_Fault_OvercurrentDischarge, ( ( (JD_VARMNGR_OBJ)item->data[2] & 0x20 ) >> 5 ), DATA_GOODDATA );
	JD_WriteVarValueStatus( CAN_11Bit_Pack3_Fault_BatteryCAN, ( ( (JD_VARMNGR_OBJ)item->data[5] & 0x08 ) >> 3 ), DATA_GOODDATA );
}

void Protections_ModFaults_Pack1_Callback(struct Std_CAN_Queue_Item_S * item)
{
}

void Protections_ModFaults_Pack2_Callback(struct Std_CAN_Queue_Item_S * item)
{
}

void Protections_ModFaults_Pack3_Callback(struct Std_CAN_Queue_Item_S * item)
{
}

void TempCoolantIn_Pack1_Callback(struct Std_CAN_Queue_Item_S * item)
{
	JD_WriteVarValueStatus( CAN_11Bit_Pack1_CoolantTempIn, ( (JD_VARMNGR_OBJ)item->data[4] ) | ( ( (JD_VARMNGR_OBJ)item->data[5] ) << 8 ), DATA_GOODDATA );
}

void TempCoolantIn_Pack2_Callback(struct Std_CAN_Queue_Item_S * item)
{
	JD_WriteVarValueStatus( CAN_11Bit_Pack2_CoolantTempIn, ( (JD_VARMNGR_OBJ)item->data[4] ) | ( ( (JD_VARMNGR_OBJ)item->data[5] ) << 8 ), DATA_GOODDATA );
}

void TempCoolantIn_Pack3_Callback(struct Std_CAN_Queue_Item_S * item)
{
	JD_WriteVarValueStatus( CAN_11Bit_Pack3_CoolantTempIn, ( (JD_VARMNGR_OBJ)item->data[4] ) | ( ( (JD_VARMNGR_OBJ)item->data[5] ) << 8 ), DATA_GOODDATA );
}

void TempCoolantOut_Pack1_Callback(struct Std_CAN_Queue_Item_S * item)
{
	JD_WriteVarValueStatus( CAN_11Bit_Pack1_CoolantTempOut, ( (JD_VARMNGR_OBJ)item->data[4] ) | ( ( (JD_VARMNGR_OBJ)item->data[5] ) << 8 ), DATA_GOODDATA );
}

void TempCoolantOut_Pack2_Callback(struct Std_CAN_Queue_Item_S * item)
{
	JD_WriteVarValueStatus( CAN_11Bit_Pack2_CoolantTempOut, ( (JD_VARMNGR_OBJ)item->data[4] ) | ( ( (JD_VARMNGR_OBJ)item->data[5] ) << 8 ), DATA_GOODDATA );
}

void TempCoolantOut_Pack3_Callback(struct Std_CAN_Queue_Item_S * item)
{
	JD_WriteVarValueStatus( CAN_11Bit_Pack3_CoolantTempOut, ( (JD_VARMNGR_OBJ)item->data[4] ) | ( ( (JD_VARMNGR_OBJ)item->data[5] ) << 8 ), DATA_GOODDATA );
}

