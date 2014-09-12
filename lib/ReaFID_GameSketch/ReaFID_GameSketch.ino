// Arduino Skript für ReaFID Spiel - sachedes 18.07.14
// Alle Systemkonfiguriationen basieren auf dem Tutorial von Cooking Hacks
// http://www.cooking-hacks.com/documentation/tutorials/rfid-13-56-mhz-nfc-module-for-arduino
//
// V 1.0

// Define Variables
uint8_t dataRX[35];//Receive buffer.
uint8_t dataTX[35];//Transmit buffer.
uint8_t _UID[4];// stores the UID (unique identifier) of a card.
uint8_t keyAccess[] = {0xFF, 0xFF, 0xFF, 0xFF, 0xFF, 0xFF } ;// stores the key or password.
uint8_t address = 0x04;//Address to read.
uint8_t ATQ[2];//Answer to request
uint8_t state;//state of the process
uint8_t aux[16];//Auxiliar buffer. 



void setup() {
  
  	//Start serial port 115200 bps:
	Serial.begin(115200);
	delay(100);
	Serial.print("RFID/NFC @ 13.56 MHz module gestartet");
	delay(1000);
	//!It is needed to launch a simple command to sycnchronize
	getFirmware();
	configureSAM();
}

void loop() {
  
 // Serial.print("\n");
 // Serial.print("Bitte waehlen Sie die Nummer fuer den Modus \n");
 // Serial.println("1 - Spiel (lesen von konfigurierten Karten)");
 // Serial.println("2 - Drittkarten konfigurieren (einlesen der UIDs)");
 // Serial.println("3 - Karten konfigurieren (Setzen des Access Key fuer leere Karten)");
 // Serial.println("4 - Karten zuruecksetzen (Entfernen des Access Key fuer leere Karten)");
  
  // Start reading
  //Serial.println("1 - Ready to read...");
  //Get the UID Identifier
	init(_UID, ATQ);
	Serial.print("\n");
	Serial.print( "***");
	print(_UID , 4);

}


//!The goal of this command is to detect as many targets (maximum MaxTg)
// as possible in passive mode.
uint8_t init(uint8_t *UID , uint8_t *ATQ)   //! Request InListPassive
{
  Serial.flush();

	dataTX[0] = 0x04; // Length
	lengthCheckSum(dataTX); // Length Checksum
	dataTX[2] = 0xD4;
	dataTX[3] = 0x4A; // Code
	dataTX[4] = 0x01; //MaxTarget
	dataTX[5] = 0x00; //BaudRate = 106Kbps
	dataTX[6] = 0x00; // Clear checkSum position
	checkSum(dataTX); 

	sendTX(dataTX , 7 ,23);

	for (int i = 17; i < (21) ; i++){
		_UID[i-17] = dataRX[i];
	UID[i-17] = _UID[i-17];
	}

	ATQ[0] = dataRX[13];
	ATQ[1] = dataRX[14];

	if ((dataRX[9]== 0xD5) & (dataRX[10] == 0x4B) & (dataRX[11] == 0x01)) {
		return 0;
	} else {
		return 1;
	}
}

//**************************************************************************************************
// Checks für initiales Setup
//!The PN532 sends back the version of the embedded firmware.
bool getFirmware(void)  //! It is needed to launch a simple command to sycnchronize
{
  Serial.print("                ");

	memset(dataTX, 0x00, 35);
	dataTX[0] = 0x02; // Length
	lengthCheckSum(dataTX); // Length Checksum
	dataTX[2] = 0xD4; // CODE
	dataTX[3] = 0x02; //TFI
	checkSum(dataTX); //0x2A; //Checksum   

	sendTX(dataTX , 5 , 17);
	Serial.print("\n");
	Serial.print("Eingesetzte Firmware version ist : ");

	for (int i = 11; i < (15) ; i++){
		Serial.print(dataRX[i], HEX);
		Serial.print(" ");
	}
	Serial.print("\n");
}

//!This command is used to set internal parameters of the PN532,
bool configureSAM(void)//! Configure the SAM
{
	Serial.print("               ");

	dataTX[0] = 0x05; //Length
	lengthCheckSum(dataTX); // Length Checksum
	dataTX[2] = 0xD4;
	dataTX[3] = 0x14;
	dataTX[4] = 0x01; // Normal mode
	dataTX[5] = 0x14; // TimeOUT
	dataTX[6] = 0x00; // IRQ
	dataTX[7] = 0x00; // Clean checkSum position
	checkSum(dataTX);

	sendTX(dataTX , 8, 13);
}
//!Calculates the checksum and stores it in dataTX buffer
void checkSum(uint8_t *dataTX)
{
	for (int i = 0; i < dataTX[0] ; i++) {
		dataTX[dataTX[0] + 2] += dataTX[i + 2];
	}
	byte(dataTX[dataTX[0] + 2]= - dataTX[dataTX[0] + 2]);
}
//!Calculates the length checksum and sotres it in the buffer.
uint8_t lengthCheckSum(uint8_t *dataTX)
{
	dataTX[1] = byte(0x100 - dataTX[0]);
}
//!Send data stored in dataTX
void sendTX(uint8_t *dataTX, uint8_t length, uint8_t outLength)
{
	Serial.print(char(0x00));
	Serial.print(char(0x00));
	Serial.print(char(0xFF)); 

	for (int i = 0; i < length; i++) {
		Serial.print(char(dataTX[i]));
	}

	Serial.print(char(0x00));
	getACK();
	waitResponse();// Receive response
	getData(outLength);
}
//!Wait for ACK response and stores it in the dataRX buffer
void getACK(void)
{
	delay(5);
	waitResponse();
	for (int i = 0; i < 5 ; i++) {
		dataRX[i] = Serial.read();
	}
}
//!Get data from the module
void getData(uint8_t outLength)
{
	for (int i=5; i < outLength; i++) {
		dataRX[i] = Serial.read();//read data from the module.
	}
}
//!Wait the response of the module
void waitResponse(void)
{
	int val = 0xFF;
	int cont = 0x00;
	while(val != 0x00) { //Wait for 0x00 response
		val = Serial.read();
		delay(5);
		cont ++;
	}
}
//!Print data stored in vectors .
void print(uint8_t * _data, uint8_t length)
{
	for (int i = 0; i < length ; i++){
		Serial.print(_data[i], HEX);
		Serial.print(" ");
	}
        Serial.print( "***");
	Serial.print("\n");
}
