# Packet-Sniffer
<h1>Description</h1>

<body>
This is a Tool which allows the user to sniff packets dynamically on desired network interface on both wired and wireless networks. The user can customize the type of packets, how long and how many packets to sniff.
</body>

<h1>Installation</h1>
<body>
git clone https://github.com/cvvardhan2002/Packet-Sniffer.git <br>
cd Packet-Sniffer <br>
</body>

<h1>Usage</h1>
<body>
Change the directory to Packet-Sniffer by using<br>
cd Packet-Sniffer<br>

![cd sniffer](https://user-images.githubusercontent.com/95639719/204135658-75d491f7-c152-49c7-9819-25b6d0073859.png)


Now to run the tool use<br>
sudo python3 packetSniffer.py<br>
Make sure to run the program with root privilages [sudo]<br>
  
![run sniffer](https://user-images.githubusercontent.com/95639719/204135681-8bf79cda-8326-4207-b54d-a981ac193294.png)

Now choose the interface on which you want to sniff the packets<br>
  
![interface sniff](https://user-images.githubusercontent.com/95639719/204135717-06ce7a52-544a-4227-80b9-31e4af85203e.png)

Choose the no of packets to be sniffed<br>
Press 0 if you dont want any limit to the packets sniffed<br>

![no packets sniff](https://user-images.githubusercontent.com/95639719/204135777-464181db-89f5-44a7-9a6d-8adc7625cc02.png)

Choose how long should the tool be sniffing packets<br>
The input is taken in the form of seconds<br>
 
![time sniff](https://user-images.githubusercontent.com/95639719/204135840-043df2a3-2573-4414-8ac3-91ed6e905739.png)

Choose the the specific protocol packets to be sniffed<br>
You can choose any one of these:<br>
1)arp<br>
2)boot<br>
3)icmp<br>
4)0 {this option is used if you want to capture all packets}<br>
  <br>

 ![protocols sniff](https://user-images.githubusercontent.com/95639719/204135937-f5ed7b26-8a14-43ed-a0f9-1acf982e5790.png)

Now choose the file where you want to save the sniffed packet logs. <br>
If no name is given it will create one file and add the data. <br>
   <br>

  ![last sniff](https://user-images.githubusercontent.com/95639719/204135976-7e7b9a76-411b-43db-ae51-03b8525c8d7e.png)
</body>

<h1>Output</h1>  
<body>
 This is a sample output of the sniffed packets stored in the file<br>

  ![file sniff](https://user-images.githubusercontent.com/95639719/204136051-dd9dd6d3-1861-4150-ab82-5f8110852be8.png)

  </body>



                                                         
