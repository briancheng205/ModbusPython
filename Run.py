from ModbusClient import *

modbusClient = ModbusClient('192.168.0.240', 502)
modbusClient.Parity = Parity.odd
modbusClient.UnitIdentifier = 1
modbusClient.Baudrate = 9600
modbusClient.Stopbits = Stopbits.one
modbusClient.Connect()
modbusClient.Parity = Parity.even
discreteInputs = modbusClient.ReadDiscreteInputs(0, 2500)
print (discreteInputs)

holdingRegisters = ConvertRegistersToFloat(modbusClient.ReadHoldingRegisters(0, 2))
print (holdingRegisters)
inputRegisters = modbusClient.ReadInputRegisters(0, 2500)
print (inputRegisters)
coils = modbusClient.ReadCoils(0, 2500)
print (coils)
modbusClient.WriteSingleCoil(0, True)
modbusClient.WriteSingleRegister(0, 777)
modbusClient.WriteMultipleCoils(0, [True,True,True,True,True,False,True])
modbusClient.WriteMultipleRegisters(0, ConvertFloatToTwoRegisters(3.141517))
modbusClient.close()
