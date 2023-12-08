#include <SPI.h>
#include <Ethernet.h>

byte mac[] = { 0xDE, 0xAD, 0xBE, 0xEF, 0xFE, 0xED }; // Dirección MAC de la Ethernet Shield
IPAddress ip(192,168,1,177); // Dirección IP asignada al Arduino
EthernetServer server(80); // Servidor Web en el puerto 80, por defecto HTTP

int LED1 = 2; // Pin del LED 1
int LED2 = 3; // Pin del LED 2
String estado1 = "OFF"; // Estado inicial del LED 1
String estado2 = "OFF"; // Estado inicial del LED 2


void setupEthernet() {
  Serial.begin(9600);
  Ethernet.begin(mac, ip);
  server.begin();
  pinMode(LED1, OUTPUT);
  pinMode(LED2, OUTPUT);
  pinMode(4, INPUT);
  pinMode(5, INPUT);
  digitalWrite(LED1, HIGH);
  digitalWrite(LED2, HIGH);
}

// Función para manejar las solicitudes HTTP y controlar los LEDs
void handleClientRequest() {
  EthernetClient client = server.available(); // Cliente Web
  if (client) {
    Serial.println("new client");
    boolean currentLineIsBlank = true;
    String cadena = "";
    while (client.connected()) {
      if (client.available()) {
        char c = client.read();
        Serial.write(c);
        if (cadena.length() < 50) {
          cadena.concat(c);
          int posicion = cadena.indexOf("Data=");
          if (cadena.substring(posicion) == "Data=1") {
            digitalWrite(LED1, LOW);
            estado1 = "ON";
          } else if (cadena.substring(posicion) == "Data=2") {
            digitalWrite(LED1, HIGH);
            estado1 = "OFF";
          } else if (cadena.substring(posicion) == "Data=3") {
            digitalWrite(LED2, LOW);
            estado2 = "ON";
          } else if (cadena.substring(posicion) == "Data=4") {
            digitalWrite(LED2, HIGH);
            estado2 = "OFF";
          }
        }
        if (c == '\n' && currentLineIsBlank) {
          sendHTTPResponse(client);
          break;
        }
        if (c == '\n') {
          currentLineIsBlank = true;
        } else if (c != '\r') {
          currentLineIsBlank = false;
        }
      }
    }
    delay(1);
    client.stop();
  }
}

// Función para enviar la respuesta HTTP al cliente
void sendHTTPResponse(EthernetClient &client) {
  client.println("HTTP/1.1 200 OK");
  client.println("Content-Type: text/html");
  client.println();
  client.println("<html>");
  client.println("<head><title>Naylamp Mechatronics</title></head>");
  client.println("<body>");
  client.println("<div style='text-align:center;'>");
  client.println("<h1>NAYLAMP MECHATRONICS</h1>");
  client.println("<h2>Entradas Analogicas</h2>");
  client.print("AN0="); client.println(analogRead(0));
  client.print("<br />AN1=");client.println(analogRead(1)); 
  client.println("<h2>Entradas Digitales</h2>");
  client.print("D4=");client.println(digitalRead(4));
  client.println("<br />D5=");client.print(digitalRead(5));
  client.println("<br /><br />");
  client.println("<a href='http://192.168.1.177'>Actualizar entradas</a>");
  client.println("<h2>Salidas Digitales </h2>");        
  client.println("Estado del LED 1 = ");client.print(estado1);            
  client.println("<br />");            
  client.print("<button onClick=location.href='./?Data=1'>ON</button>");           
  client.print("<button onClick=location.href='./?Data=2'>OFF</button>");
  client.println("<br /><br />");
  client.println("Estado del LED 2 = ");client.print(estado2);            
  client.println("<br />");            
  client.print("<button onClick=location.href='./?Data=3'>ON</button>");           
  client.print("<button onClick=location.href='./?Data=4'>OFF</button>");
  client.println("<br /><br />");
  client.println("<a href='https://naylampmechatronics.com/'>naylampmechatronics.com</a>");
  client.println("<br /><br />");             
  client.println("</body>");
  client.println("</html>");
}

void setup() {
  setupEthernet();
}

void loop() {
  handleClientRequest();
}
