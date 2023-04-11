void Vitals_PackVoltageCurrent_Pack1_Callback(struct Std_CAN_Queue_Item_S * item)
{
	JD_WriteVarValueStatus( CAN_11Bit_Pack1_Voltage, ( (UInt16_T)item->data[0] ) | ( ( (UInt16_T)item->data[1] ) << 8 ), DATA_GOODDATA );
	JD_WriteVarValueStatus( CAN_11Bit_Pack1_Current, ( (UInt16_T)item->data[2] ) | ( ( (UInt16_T)item->data[3] ) << 8 ), DATA_GOODDATA );
	JD_WriteVarValueStatus( CAN_11Bit_Pack1_DCBusVoltage, ( (UInt16_T)item->data[4] ) | ( ( (UInt16_T)item->data[5] ) << 8 ), DATA_GOODDATA );
}

void Vitals_PackVoltageCurrent_Pack2_Callback(struct Std_CAN_Queue_Item_S * item)
{
	JD_WriteVarValueStatus( CAN_11Bit_Pack2_Voltage, ( (UInt16_T)item->data[0] ) | ( ( (UInt16_T)item->data[1] ) << 8 ), DATA_GOODDATA );
	JD_WriteVarValueStatus( CAN_11Bit_Pack2_Current, ( (UInt16_T)item->data[2] ) | ( ( (UInt16_T)item->data[3] ) << 8 ), DATA_GOODDATA );
	JD_WriteVarValueStatus( CAN_11Bit_Pack2_DCBusVoltage, ( (UInt16_T)item->data[4] ) | ( ( (UInt16_T)item->data[5] ) << 8 ), DATA_GOODDATA );
}

void Vitals_PackVoltageCurrent_Pack3_Callback(struct Std_CAN_Queue_Item_S * item)
{
	JD_WriteVarValueStatus( CAN_11Bit_Pack3_Voltage, ( (UInt16_T)item->data[0] ) | ( ( (UInt16_T)item->data[1] ) << 8 ), DATA_GOODDATA );
	JD_WriteVarValueStatus( CAN_11Bit_Pack3_Current, ( (UInt16_T)item->data[2] ) | ( ( (UInt16_T)item->data[3] ) << 8 ), DATA_GOODDATA );
	JD_WriteVarValueStatus( CAN_11Bit_Pack3_DCBusVoltage, ( (UInt16_T)item->data[4] ) | ( ( (UInt16_T)item->data[5] ) << 8 ), DATA_GOODDATA );
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
	JD_WriteVarValueStatus( CAN_11Bit_Pack1_MaxCurrentDischarge, ( (UInt16_T)item->data[0] ) | ( ( (UInt16_T)item->data[1] ) << 8 ), DATA_GOODDATA );
	JD_WriteVarValueStatus( CAN_11Bit_Pack1_MaxCurrentCharge, ( (UInt16_T)item->data[2] ) | ( ( (UInt16_T)item->data[3] ) << 8 ), DATA_GOODDATA );
}

void PowerLimits_MaxChgDschgCurr_Pack2_Callback(struct Std_CAN_Queue_Item_S * item)
{
	JD_WriteVarValueStatus( CAN_11Bit_Pack2_MaxCurrentDischarge, ( (UInt16_T)item->data[0] ) | ( ( (UInt16_T)item->data[1] ) << 8 ), DATA_GOODDATA );
	JD_WriteVarValueStatus( CAN_11Bit_Pack2_MaxCurrentCharge, ( (UInt16_T)item->data[2] ) | ( ( (UInt16_T)item->data[3] ) << 8 ), DATA_GOODDATA );
}

void PowerLimits_MaxChgDschgCurr_Pack3_Callback(struct Std_CAN_Queue_Item_S * item)
{
	JD_WriteVarValueStatus( CAN_11Bit_Pack3_MaxCurrentDischarge, ( (UInt16_T)item->data[0] ) | ( ( (UInt16_T)item->data[1] ) << 8 ), DATA_GOODDATA );
	JD_WriteVarValueStatus( CAN_11Bit_Pack3_MaxCurrentCharge, ( (UInt16_T)item->data[2] ) | ( ( (UInt16_T)item->data[3] ) << 8 ), DATA_GOODDATA );
}

void VoltStatsBlock_CellVoltage_Pack1_Callback(struct Std_CAN_Queue_Item_S * item)
{
	JD_WriteVarValueStatus( CAN_11Bit_Pack1_MinCellVoltage, ( (UInt16_T)item->data[0] ) | ( ( (UInt16_T)item->data[1] ) << 8 ), DATA_GOODDATA );
	JD_WriteVarValueStatus( CAN_11Bit_Pack1_MaxCellVoltage, ( (UInt16_T)item->data[2] ) | ( ( (UInt16_T)item->data[3] ) << 8 ), DATA_GOODDATA );
}

void VoltStatsBlock_CellVoltage_Pack2_Callback(struct Std_CAN_Queue_Item_S * item)
{
	JD_WriteVarValueStatus( CAN_11Bit_Pack2_MinCellVoltage, ( (UInt16_T)item->data[0] ) | ( ( (UInt16_T)item->data[1] ) << 8 ), DATA_GOODDATA );
	JD_WriteVarValueStatus( CAN_11Bit_Pack2_MaxCellVoltage, ( (UInt16_T)item->data[2] ) | ( ( (UInt16_T)item->data[3] ) << 8 ), DATA_GOODDATA );
}

void VoltStatsBlock_CellVoltage_Pack3_Callback(struct Std_CAN_Queue_Item_S * item)
{
	JD_WriteVarValueStatus( CAN_11Bit_Pack3_MinCellVoltage, ( (UInt16_T)item->data[0] ) | ( ( (UInt16_T)item->data[1] ) << 8 ), DATA_GOODDATA );
	JD_WriteVarValueStatus( CAN_11Bit_Pack3_MaxCellVoltage, ( (UInt16_T)item->data[2] ) | ( ( (UInt16_T)item->data[3] ) << 8 ), DATA_GOODDATA );
}

void TempCell_CellTemp_Pack1_Callback(struct Std_CAN_Queue_Item_S * item)
{
	JD_WriteVarValueStatus( CAN_11Bit_Pack1_MinCellTemp, ( (UInt16_T)item->data[0] ) | ( ( (UInt16_T)item->data[1] ) << 8 ), DATA_GOODDATA );
	JD_WriteVarValueStatus( CAN_11Bit_Pack1_MaxCellTemp, ( (UInt16_T)item->data[2] ) | ( ( (UInt16_T)item->data[3] ) << 8 ), DATA_GOODDATA );
	JD_WriteVarValueStatus( CAN_11Bit_Pack1_AvgCellTemp, ( (UInt16_T)item->data[4] ) | ( ( (UInt16_T)item->data[5] ) << 8 ), DATA_GOODDATA );
}

void TempCell_CellTemp_Pack2_Callback(struct Std_CAN_Queue_Item_S * item)
{
	JD_WriteVarValueStatus( CAN_11Bit_Pack2_MinCellTemp, ( (UInt16_T)item->data[0] ) | ( ( (UInt16_T)item->data[1] ) << 8 ), DATA_GOODDATA );
	JD_WriteVarValueStatus( CAN_11Bit_Pack2_MaxCellTemp, ( (UInt16_T)item->data[2] ) | ( ( (UInt16_T)item->data[3] ) << 8 ), DATA_GOODDATA );
	JD_WriteVarValueStatus( CAN_11Bit_Pack2_AvgCellTemp, ( (UInt16_T)item->data[4] ) | ( ( (UInt16_T)item->data[5] ) << 8 ), DATA_GOODDATA );
}

void TempCell_CellTemp_Pack3_Callback(struct Std_CAN_Queue_Item_S * item)
{
	JD_WriteVarValueStatus( CAN_11Bit_Pack3_MinCellTemp, ( (UInt16_T)item->data[0] ) | ( ( (UInt16_T)item->data[1] ) << 8 ), DATA_GOODDATA );
	JD_WriteVarValueStatus( CAN_11Bit_Pack3_MaxCellTemp, ( (UInt16_T)item->data[2] ) | ( ( (UInt16_T)item->data[3] ) << 8 ), DATA_GOODDATA );
	JD_WriteVarValueStatus( CAN_11Bit_Pack3_AvgCellTemp, ( (UInt16_T)item->data[4] ) | ( ( (UInt16_T)item->data[5] ) << 8 ), DATA_GOODDATA );
}

void StressEst_Pack1_Callback(struct Std_CAN_Queue_Item_S * item)
{
	JD_WriteVarValueStatus( CAN_11Bit_Pack1_StressEst_Charge, ( (UInt16_T)item->data[0] ) | ( ( (UInt16_T)item->data[1] ) << 8 ), DATA_GOODDATA );
	JD_WriteVarValueStatus( CAN_11Bit_Pack1_StressEst_Discharge, ( (UInt16_T)item->data[2] ) | ( ( (UInt16_T)item->data[3] ) << 8 ), DATA_GOODDATA );
}

void StressEst_Pack2_Callback(struct Std_CAN_Queue_Item_S * item)
{
	JD_WriteVarValueStatus( CAN_11Bit_Pack2_StressEst_Charge, ( (UInt16_T)item->data[0] ) | ( ( (UInt16_T)item->data[1] ) << 8 ), DATA_GOODDATA );
	JD_WriteVarValueStatus( CAN_11Bit_Pack2_StressEst_Discharge, ( (UInt16_T)item->data[2] ) | ( ( (UInt16_T)item->data[3] ) << 8 ), DATA_GOODDATA );
}

void StressEst_Pack3_Callback(struct Std_CAN_Queue_Item_S * item)
{
	JD_WriteVarValueStatus( CAN_11Bit_Pack3_StressEst_Charge, ( (UInt16_T)item->data[0] ) | ( ( (UInt16_T)item->data[1] ) << 8 ), DATA_GOODDATA );
	JD_WriteVarValueStatus( CAN_11Bit_Pack3_StressEst_Discharge, ( (UInt16_T)item->data[2] ) | ( ( (UInt16_T)item->data[3] ) << 8 ), DATA_GOODDATA );
}

void IsolationStatus_Pack1_Callback(struct Std_CAN_Queue_Item_S * item)
{
}

void IsolationStatus_Pack2_Callback(struct Std_CAN_Queue_Item_S * item)
{
}

void IsolationStatus_Pack3_Callback(struct Std_CAN_Queue_Item_S * item)
{
}

void Protections_BMSFaults_Pack1_Callback(struct Std_CAN_Queue_Item_S * item)
{
}

void Protections_BMSFaults_Pack2_Callback(struct Std_CAN_Queue_Item_S * item)
{
}

void Protections_BMSFaults_Pack3_Callback(struct Std_CAN_Queue_Item_S * item)
{
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
	JD_WriteVarValueStatus( CAN_11Bit_Pack1_CoolantTempIn, ( (UInt16_T)item->data[4] ) | ( ( (UInt16_T)item->data[5] ) << 8 ), DATA_GOODDATA );
}

void TempCoolantIn_Pack2_Callback(struct Std_CAN_Queue_Item_S * item)
{
	JD_WriteVarValueStatus( CAN_11Bit_Pack2_CoolantTempIn, ( (UInt16_T)item->data[4] ) | ( ( (UInt16_T)item->data[5] ) << 8 ), DATA_GOODDATA );
}

void TempCoolantIn_Pack3_Callback(struct Std_CAN_Queue_Item_S * item)
{
	JD_WriteVarValueStatus( CAN_11Bit_Pack3_CoolantTempIn, ( (UInt16_T)item->data[4] ) | ( ( (UInt16_T)item->data[5] ) << 8 ), DATA_GOODDATA );
}

void TempCoolantOut_Pack1_Callback(struct Std_CAN_Queue_Item_S * item)
{
	JD_WriteVarValueStatus( CAN_11Bit_Pack1_CoolantTempOut, ( (UInt16_T)item->data[4] ) | ( ( (UInt16_T)item->data[5] ) << 8 ), DATA_GOODDATA );
}

void TempCoolantOut_Pack2_Callback(struct Std_CAN_Queue_Item_S * item)
{
	JD_WriteVarValueStatus( CAN_11Bit_Pack2_CoolantTempOut, ( (UInt16_T)item->data[4] ) | ( ( (UInt16_T)item->data[5] ) << 8 ), DATA_GOODDATA );
}

void TempCoolantOut_Pack3_Callback(struct Std_CAN_Queue_Item_S * item)
{
	JD_WriteVarValueStatus( CAN_11Bit_Pack3_CoolantTempOut, ( (UInt16_T)item->data[4] ) | ( ( (UInt16_T)item->data[5] ) << 8 ), DATA_GOODDATA );
}

