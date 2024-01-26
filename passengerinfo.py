import csv
class PassengerRegisteration():
    #constructor
   def __init__(self):
        self.PassengerName =None
        self.noOfPassenger = None
        self.departureLocation = None
        self.destinstionLocation = None
        self.ddmmyyyy =None
        self.seatNo = None
        self.selectBusType = None
        self.autoInc = 1
        self.counycol=0
    
def getPassengerInfo(self):
        self.PassengerName = input(" Enter Passenger NAme :")
        self.noOfPassenger =int(input("Enter Number Of Passenger :"))
        print("1:-Nagpur")
        print("2:-pune")
        print("3:-Mumbai")
        print("4:-Delhi")

        #enter departure location name start
        self.__init__(input("Enter Departure Location"))
        if self.d1==1:
            self.departureLocation = "Nagpur"
        elif self.d1==2:
            self.departureLocation = "Pune"
        elif self.d1==3:
            self.departureLocation = "Mumbai"
        elif self.d1==4:
            self.departureLocation = "Delhi"
        else:
            print("Please Enter Correct Choice")

            # departire location name end

        print("1:-Gujrat")
        print("2:-Raipur")
        print("3:-Patana")
        print("4:-Bhopal")

        # enter destination location name start

        self.dp1=int(int("Entyer Destination Location:"))
        if self.dp1==1:
         self.destinationLocation = "Gujrat"
        elif self.dp1==2:
         self.destinationLocation = "Raipur"
        elif self.dp1==3:
         self.destinationLocation = "Patana"
        elif self.dp1==4:
         self.destinationLocation = "Bhopal"

        self.ddmmyyyy = input("Enetr Date Of Joiurney Like 06-03-2002")

        #Booking seat start
        print("[1]_[2]_[3]_[4]_[5]_[6]_[7]_[8]_[9]_[10]")
        print("[11]_[12]_[13]_[14]_[15]_[16]_[17]_[18]_[19]_[20]")
        print("[21]_[22]_[23]_[24]_[25]_[26]_[27]_[28]_[29]_[30]")

        seatNoList=[1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20,21,22,23,24,25,26,27,28,29,30]
        self.bookingList=[]
        while True:
           self.seatNo=int(input("Choose a Seat Number & Max To Max You Can Book Two Ticket : "))
           if self.seatNo<=30:
              
              if self.seatNo in seatNoList:
                 self.bookingList.append(self.seatNo)
                 del seatNoList[self.seatNo+1]
                 count = len(seatNoList)
              else:
                 print("Ticket Allready Booked")
                 print("Do You Want To Book One More Seat Enter (Yes/No)")
              y=input ("")
              if y == "Yes":
                 pass
              else:
                 break
              
           else:
              print("1.AC BUS = 500 RS Fare")
              print("2.NON AC BUS = 300 RS Fare " )
              self.busType = int(input("Select Bus Type :"))

              if self.busType == 1:
                 self.selectBusType = "AC BUS"
                 self.busFare =self.noOfPassenger*500
              elif self.busType==2:
                 self.selectBusType ="NON AC BUS"
                 self.busFare =self.noOfPassenger*300


                 #bookikng seat end




class PassengerDataCav(PassengerRegisteration):
   def saveInfo(self):
        
           with open("passengerData.csv",'r+',newLine="") as f:
              r = csv.reader(f)
              data = list(r)
              for i in data:
                 self.autoInc +=1
                 for j in i:
                    self.countcol +=1
                    print()
                    print(" Number Of Rrecord Are found In Data base:",self.autoInc)
