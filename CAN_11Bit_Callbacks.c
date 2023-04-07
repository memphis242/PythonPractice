void Vitals_PackVoltageCurrent_Callback(struct Std_CAN_Queue_Item_S * item)
{
	JD_WriteVarValueStatus( CAN_11Bit_Pack1_Voltage, , ( ( (UInt16_T)item->data[1] ) << 8 ) | ( (UInt16_T)item->data[0] ), DATA_GOODDATA );
	JD_WriteVarValueStatus( CAN_11Bit_Pack1_Current, , ( ( (UInt16_T)item->data[3] ) << 8 ) | ( (UInt16_T)item->data[2] ), DATA_GOODDATA );
	JD_WriteVarValueStatus( CAN_11Bit_Pack1_DCBusVoltage, , ( ( (UInt16_T)item->data[5] ) << 8 ) | ( (UInt16_T)item->data[4] ), DATA_GOODDATA );
}

