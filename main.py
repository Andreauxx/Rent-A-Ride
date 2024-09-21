import time
from rich.table import Table
from rich.panel import Panel
from rich.progress import Progress
from rich.text import Text
from rich import print as rprint
#JEONANDREAUX
CustomerName = []
CustomerAge=[]
CustomerGender=[]
IDType=[]
IDNumber=[]
name,age,gender,idtype,idnumber="",0,"","",0

RentedCarID = []
RentedCarBrand = []
RentedCarModel = []
RentedCarType = []
RentedCarPrice = []
RentedDays = []

earnings = 0

CarID = [1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20]

CarBrand = ["Toyota", "Honda", "Ford", "BMW", "Chevrolet", "Tesla", "Mercedes-Benz", "Porsche", "Audi", "Jeep", "Ferrari", "Hyundai", "McLaren", "Subaru", "Lamborghini", "Kia", "Aston Martin", "Nissan", "Bugatti", "Volvo"]

CarModel = ["Camry", "Civic", "Mustang", "3 Series", "Corvette", "Model 3", "S-Class", "911", "Q5", "Wrangler", "488 GTB", "Santa Fe", "720S", "Outback", "Aventador", "Telluride", "DB11", "Rogue", "Chiron", "XC90"]

CarType = ["Sedan", "Coupe", "Convertible", "Luxury Sedan", "Sports Car", "Electric Sedan", "Luxury Sedan", "Supercar", "SUV", "Off-Road SUV", "Supercar", "SUV", "Supercar", "Crossover", "Supercar", "SUV", "Grand Tourer", "Compact SUV", "Hypercar", "Luxury SUV"]

CarPrice = [7500, 6000, 9000, 11250, 15000, 9000, 13500, 18750, 12000, 6750, 37500, 8250, 22500, 7125, 45000, 9750, 26250, 9000, 150000, 13500, 11250]


def welcomefunction():
    message = Text("Hello! Welcome to Rent-A-Ride, your go-to car rental destination! "
                   "\nExperience seamless journeys with our diverse collection "
                   "\nFrom sleek sedans to rugged SUVs and adrenaline-pumping supercars "
                   "\nWe've got the wheels for every adventure. "
                   "\nPress Enter To Continue")
    welcome_message = Panel(Text(f"{message}",justify="center",style="bold bright_cyan"),title="RENT-A-RIDE",border_style="bold green")
    rprint(welcome_message)
    input("                                                                                             ")
def menu():
   Menu = Text("Please type a number to choose"
               "\n1.Add Customers "
               "\n2.Display Customers "
               "\n3.Customer Return "
               "\n4.Search Customer "
               "\n5.Update Customer "
               "\n6.Add Cars "
               "\n7.Display Cars "
               "\n8.Update Cars "
               "\n9.Remove Car "
               "\n10.Search Car "
               "\n11.Total Earnings "
               "\nPress Any Key to exit")
   panelMenu =Panel(Text(f"{Menu}",justify="center",style="bold bright_cyan"),title="MENU",border_style="bold green",title_align="center")
   rprint(panelMenu)

def AddCar():
    panel_choice = Panel(
        Text("ENTER CAR ID (START AT 21)", justify="center", style="bold bright_cyan"),
        title="UPDATE!",

        border_style="bold green",
    )
    rprint(panel_choice)
    carID = int(input("                                                                                                                    "))
    if carID in CarID:
        panel_choice = Panel(
            Text("CAR ID ALREADY EXISTS", justify="center", style="bold bright_cyan"),
            title="UPDATE!",
            border_style="bold green",
        )
        rprint(panel_choice)
    else:
        panel_choice = Panel(
            Text("ENTER CAR BRAND", justify="center", style="bold bright_cyan"),
            title="UPDATE!",
            border_style="bold green",
        )
        rprint(panel_choice)
        carBrand = input("                                                                                                                   ")
        panel_choice = Panel(
            Text("ENTER CAR MODEL", justify="center", style="bold bright_cyan"),
            title="UPDATE!",
            border_style="bold green",
        )
        rprint(panel_choice)
        carModel = input("                                                                                                                   ")
        panel_choice = Panel(
            Text("ENTER CAR TYPE", justify="center", style="bold bright_cyan"),
            title="UPDATE!",
            border_style="bold green",
        )
        rprint(panel_choice)
        carType = input("                                                                                                                   ")
        panel_choice = Panel(
            Text("ENTER CAR PRICE", justify="center", style="bold bright_cyan"),
            title="UPDATE!",
            border_style="bold green",
        )
        rprint(panel_choice)
        carPrice = int(input("                                                                                                                    "))

        CarID.append(carID)
        CarBrand.append(carBrand)
        CarModel.append(carModel)
        CarType.append(carType)
        CarPrice.append(carPrice)

        with Progress() as progress:
            task = progress.add_task(
                "                                                                                   [cyan]Adding Car...",
                total=100, style="bar")
            for i in range(100):
                time.sleep(0.01)
                progress.update(task, advance=1)



        panel_choice = Panel(
            Text(str("Car Added Successfully!"), justify="center", style="bold bright_cyan"),
            title="UPDATE",
            border_style="bold green",
        )
        rprint(panel_choice)

def AddCustomer():
    global earnings
    while True:
        name = input("                                                                                    Name:\t")

        if name.isdigit():
            msg18 = Panel(Text("Names Cannot Be A Number!"
                               "",justify="center",style="bold bright cyan"),title="RESPONSE",border_style="bold green")
            rprint(msg18)
            break

        age = input("                                                                                     Age:\t")

        if age.isdigit():
            age = int(age)

            if age < 18:
                msg18 = Panel(Text("You are under aged you are not allowed to rent a car! You can just view them.",justify="center",style="bold bright cyan"),title="RESPONSE",border_style="bold green")
                rprint(msg18)
                break


            gender = input(
                    "                                                                                  Gender:\t")
            idtype = input(
                    "                                                                                 ID Type:\t")
            idnumber = input(
                    "                                                                               ID Number:\t")

            if idnumber.isdigit():

                idnumber = int(idnumber)
                if idnumber in IDNumber:
                    exist = Panel(
                            Text("This ID Number Already Exist!", justify="center",
                                 style="bold bright cyan"), title="RESPONSE", border_style="bold green")
                    rprint(exist)
                    break



                DisplayCars()
                choosecar = input("                                                                                     |Enter your choice|: ")
                validchoice= True

                panel_choice = Panel(
                        Text(str(choosecar), justify="center", style="bold bright_cyan"),
                        title="Chosen Car",
                        border_style="bold green",
                    )
                rprint(panel_choice)

                if choosecar.isdigit():
                    choosecar = int(choosecar)
                    if choosecar in RentedCarID or choosecar not in CarID:
                        validchoice = False
                        panel_choice = Panel(
                            Text("The Car You Chose is Not Available", justify="center", style="bold bright_cyan"),
                            title="UPDATE",
                            border_style="bold green")
                        rprint(panel_choice)


                    if validchoice:
                        CustomerName.append(name)
                        CustomerAge.append(age)
                        CustomerGender.append(gender)
                        IDType.append(idtype)
                        IDNumber.append(idnumber)
                        index = CarID.index(choosecar)
                        days_rent = int(input("                                                                                      |How many days?|: "))
                        earn = days_rent * CarPrice[index]
                        chosen_car_brand = CarBrand.pop(index)
                        chosen_car_id = CarID.pop(index)
                        chosen_car_type = CarType.pop(index)
                        chosen_car_model = CarModel.pop(index)
                        chosen_car_price = CarPrice.pop(index)
                        # Append the stored values to RentedCar lists
                        RentedCarBrand.append(chosen_car_brand)
                        RentedCarID.append(chosen_car_id)
                        RentedCarType.append(chosen_car_type)
                        RentedCarModel.append(chosen_car_model)
                        RentedCarPrice.append(chosen_car_price)
                        RentedDays.append(days_rent)
                        earnings += earn

                        with Progress() as progress:
                            task = progress.add_task("                                                             [cyan]Adding the Customer...", total=100,style="bar")
                            for i in range(200):
                                time.sleep(0.01)
                                progress.update(task, advance=1)


                        panel_choice = Panel(
                            Text(str("Customer Added Successfully!"), justify="center", style="bold bright_cyan"),
                            title="UPDATE",
                            border_style="bold green",
                        )
                        rprint(panel_choice)
                        break

                else:
                    panel_choice = Panel(
                        Text("Invalid Car ID. Please choose a valid car.", justify="center", style="bold bright_cyan"),
                        title="UPDATE",
                        border_style="bold green"
                    )
                    rprint(panel_choice)
            else:
                msg18 = Panel(
                    Text("Your id number should only contain numbers!.", justify="center",
                         style="bold bright cyan"), title="RESPONSE", border_style="bold green")
                rprint(msg18)
                break
        else:
            msg18 = Panel(
                Text("Your age should be a number!.", justify="center",
                     style="bold bright cyan"), title="RESPONSE", border_style="bold green")
            rprint(msg18)
            break

def DisplayCars():
    table1 = Table(title="Car List",title_justify="center",width=185)
    table1.add_column("Car ID", justify="center", style="magenta",header_style="bold magenta")
    table1.add_column("Car Brand",justify="center",style="cyan",header_style="bold cyan")
    table1.add_column("Car Model", justify="center", style="red",header_style="bold red")
    table1.add_column("Car Type", justify="center", style="green",header_style="bold green")
    table1.add_column("Car Price", justify="center", style="blue",header_style="bold blue")

    car_list_length = len(CarBrand)
    for i in range(car_list_length):
        table1.add_row(str(CarID[i]),CarBrand[i],CarModel[i],CarType[i],str(CarPrice[i]))

    rprint(table1)


def DisplayCustomers():
    table = Table(title="Customer List",title_justify="center",width=185)
    table.add_column("Name",justify="center",style="cyan",header_style="bold cyan")
    table.add_column("Age",justify="center",style="red",header_style="bold red")
    table.add_column("Gender",justify="center",style="green",header_style="bold green")
    table.add_column("ID Type",justify="center",style="blue",header_style="bold blue")
    table.add_column("ID Number",justify="center",style="yellow",header_style="bold yellow")

    for i in range(len(CustomerName)):
        table.add_row(CustomerName[i],str(CustomerAge[i]),CustomerGender[i],IDType[i],str(IDNumber[i]))

    table.add_column("Car Brand Rented", justify="center", style="cyan",header_style="bold cyan")
    table.add_column("Car ID Rented", justify="center", style="blue",header_style="bold blue")
    table.add_column("Car Model Rented", justify="center", style="red",header_style="bold red")
    table.add_column("Car Type Rented", justify="center", style="green",header_style="bold green")
    table.add_column("Car Rented Price", justify="center", style="yellow",header_style="bold yellow")
    table.add_column("Days Rented", justify="center", style="blue",header_style="bold blue")
    for i in range(len(RentedCarModel)):
        table.add_row(
            '',
            '',
            '',
            '',
            '',
            str(RentedCarBrand[i]),
            str(RentedCarID[i]),
            str(RentedCarModel[i]),
            str(RentedCarType[i]),
            str(RentedCarPrice[i]),
            str(RentedDays[i])
        )
    rprint(table)

def CustomerReturn():
    remove = input("                                                                              Type Name or ID Number to Return:")
    if remove.isalpha():
        if remove in CustomerName:
            i = CustomerName.index(remove)
            CustomerName.pop(i)
            CustomerAge.pop(i)
            CustomerGender.pop(i)
            IDNumber.pop(i)
            IDType.pop(i)

            returned_car_id = RentedCarID.pop(i)
            returned_car_brand = RentedCarBrand.pop(i)
            returned_car_model = RentedCarModel.pop(i)
            returned_car_type = RentedCarType.pop(i)
            returned_car_price = RentedCarPrice.pop(i)
            RentedDays.pop(i)


            CarID.append(returned_car_id)
            CarBrand.append(returned_car_brand)
            CarModel.append(returned_car_model)
            CarType.append(returned_car_type)
            CarPrice.append(returned_car_price)


            with Progress() as progress:
                task = progress.add_task(
                    "                                                                [cyan]Updating..",
                    total=100, style="bar")
                for i in range(200):
                    time.sleep(0.01)
                    progress.update(task, advance=1)

            panel_choice = Panel(
                Text(str("Customer Has Returned the Car Successfully!"), justify="center", style="bold bright_cyan"),
                title="UPDATE",
                border_style="bold green",
            )
            rprint(panel_choice)

        else:
            panel_choice = Panel(
                Text(str("Customer Does Not Exist!"), justify="center", style="bold bright_cyan"),
                title="UPDATE",
                border_style="bold green",
            )
            rprint(panel_choice)

    elif remove.isdigit():
        remove = int(remove)
        if remove in IDNumber:
            i = IDNumber.index(remove)
            CustomerName.pop(i)
            CustomerAge.pop(i)
            CustomerGender.pop(i)
            IDNumber.pop(i)
            IDType.pop(i)

            returned_car_id = RentedCarID.pop(i)
            returned_car_brand = RentedCarBrand.pop(i)
            returned_car_model = RentedCarModel.pop(i)
            returned_car_type = RentedCarType.pop(i)
            returned_car_price = RentedCarPrice.pop(i)
            RentedDays.pop(i)

            # Append the returned values to the original lists
            CarID.append(returned_car_id)
            CarBrand.append(returned_car_brand)
            CarModel.append(returned_car_model)
            CarType.append(returned_car_type)
            CarPrice.append(returned_car_price)





            with Progress() as progress:
                task = progress.add_task(
                    "                                                                [cyan]Updating..",
                    total=100, style="bar")
                for i in range(200):
                    time.sleep(0.01)
                    progress.update(task, advance=1)

            panel_choice = Panel(
                Text(str("Customer Has Returned the Car Successfully!"), justify="center", style="bold bright_cyan"),
                title="UPDATE",
                border_style="bold green",
            )
            rprint(panel_choice)
        else:
            panel_choice = Panel(
                Text(str("Customer Does Not Exist!"), justify="center", style="bold bright_cyan"),
                title="UPDATE",
                border_style="bold green",
            )
            rprint(panel_choice)

def RemoveCar():
    remove = int(input("                                                                                   Type Car ID to Remove: "))
    if remove in CarID:
        i = CarID.index(remove)
        CarID.pop(i)
        CarBrand.pop(i)
        CarModel.pop(i)
        CarType.pop(i)
        CarPrice.pop(i)

    with Progress() as progress:
        task = progress.add_task(
            "                                                               [cyan]Removing..",
            total=100, style="bar")
        for i in range(100):
            time.sleep(0.01)
            progress.update(task, advance=1)

    panel_choice = Panel(
        Text(str("Car Has Been Removed Successfully!"), justify="center", style="bold bright_cyan"),
        title="UPDATE",
        border_style="bold green",
    )
    rprint(panel_choice)

def choosemenu():
    while True:
        menu()
        user_input = (input("                                                                                     |Enter your choice|: "))

        if user_input == '1':
            panel_choice = Panel(
                Text("1.Add Customer", justify="center", style="bold bright_cyan"),
                title="CHOSEN MENU",
                border_style="bold green",
            )
            rprint(panel_choice)
            print("\n")
            AddCustomer()

        elif user_input == '2':
            panel_choice = Panel(
                Text("2. Display Customers", justify="center", style="bold bright_cyan"),
                title="CHOSEN MENU",
                border_style="bold green",
            )
            rprint(panel_choice)
            print("")
            DisplayCustomers()

        elif user_input == '3':
            panel_choice = Panel(
                Text("3. Customer Return", justify="center", style="bold bright_cyan"),
                title="CHOSEN MENU",
                border_style="bold green",
            )
            rprint(panel_choice)
            print("\n")
            CustomerReturn()

        elif user_input == '4':
            panel_choice = Panel(
                Text("4. Search Customer", justify="center", style="bold bright_cyan"),
                title="CHOSEN MENU",
                border_style="bold green",
            )
            rprint(panel_choice)
            print("\n")
            SearchCustomer()

        elif user_input == '5':
            panel_choice = Panel(
                Text("5. Update Customer", justify="center", style="bold bright_cyan"),
                title="CHOSEN MENU",
                border_style="bold green",
            )
            rprint(panel_choice)
            print("\n")
            UpdateCustomer()

        elif user_input == '6':
            panel_choice = Panel(
                Text("6. Add Cars", justify="center", style="bold bright_cyan"),
                title="CHOSEN MENU",
                border_style="bold green",
            )
            rprint(panel_choice)
            print("\n")
            AddCar()

        elif user_input == '7':
            panel_choice = Panel(
                Text("7. Display Cars", justify="center", style="bold bright_cyan"),
                title="CHOSEN MENU",
                border_style="bold green",
            )
            rprint(panel_choice)
            print("")
            DisplayCars()


        elif user_input == '8':
            panel_choice = Panel(
                Text("8. Update Cars", justify="center", style="bold bright_cyan"),
                title="CHOSEN MENU",
                border_style="bold green",
            )
            rprint(panel_choice)
            print("\n")
            UpdateCar()


        elif user_input == '9':
            panel_choice = Panel(
                Text("9.Remove Cars", justify="center", style="bold bright_cyan"),
                title="CHOSEN MENU",
                border_style="bold green",
            )
            rprint(panel_choice)
            print("\n")
            RemoveCar()

        elif user_input == '10':
            panel_choice = Panel(
                Text("10. Search Cars", justify="center", style="bold bright_cyan"),
                title="CHOSEN MENU",
                border_style="bold green",
            )
            rprint(panel_choice)
            print("\n")
            SearchCars()

        elif user_input == '11':
            panel_choice = Panel(
                Text("10. Total Earnings", justify="center", style="bold bright_cyan"),
                title="CHOSEN MENU",
                border_style="bold green",
            )
            rprint(panel_choice)
            print("\n")
            ShowEarnings()


        else:
            panel_choice = Panel(
                Text("EXIT", justify="center", style="bold bright_cyan"),
                title="CHOSEN MENU",
                border_style="bold green",
            )
            rprint(panel_choice)
            with Progress() as progress:
                task = progress.add_task(
                    "                                                             [cyan]Exiting..",
                    total=100, style="bar")
                for i in range(250):
                    time.sleep(0.01)
                    progress.update(task, advance=1)

                progress.update(task, completed=100, complete_style="complete")

            rprint("                                                                                     [bold green]Enjoy the Ride![/bold green]")
            break

def UpdateCustomer():
    id = input("                                                                                Type ID Number to Update: ")

    if id.isdigit():
        id = int(id)
        if id in IDNumber:
            i = IDNumber.index(id)
            cname = Panel(
                Text(f"Enter New Name for {CustomerName[i]}", justify="center", style="bold bright_cyan"),
                title="UPDATE!",
                border_style="bold green",
            )
            rprint(cname)
            CustomerName[i] = input(f"                                                                                      ")
            cname = Panel(
                Text(f"Enter New Age for {CustomerAge[i]}", justify="center", style="bold bright_cyan"),
                title="UPDATE!",
                border_style="bold green",
            )
            rprint(cname)
            cage = input(f"                                                                                                ")

            if cage.isdigit():
                CustomerAge[i] = int(cage)
                cname = Panel(
                    Text(f"Enter New Gender for {CustomerGender[i]}", justify="center", style="bold bright_cyan"),
                    title="UPDATE!",
                    border_style="bold green",
                )
                rprint(cname)
                CustomerGender[i] = input(f"                                                                                             ")
                cname = Panel(
                    Text(f"Enter New ID Type for {IDType[i]}", justify="center", style="bold bright_cyan"),
                    title="UPDATE!",
                    border_style="bold green",
                )
                rprint(cname)
                IDType[i] = input(f"                                                                                         ")
                cname = Panel(
                    Text(f"Enter New ID Number for {IDNumber[i]}", justify="center", style="bold bright_cyan"),
                    title="UPDATE!",
                    border_style="bold green",
                )
                rprint(cname)
                idnum=input(f"                          "
                            f"                                                                     ")

                if idnum.isdigit():
                    idnum = int(idnum)
                    if idnum in IDNumber:
                        panel_choice = Panel(
                            Text("ID Number already exists! Will Stay With the Previous ID Number", justify="center", style="bold bright_cyan"),
                            title="UPDATE!",
                            border_style="bold green",
                        )
                        rprint(panel_choice)

                    else:
                        IDNumber[i] = int(idnum)

                        with Progress() as progress:
                            task = progress.add_task(
                                "                                                                             [cyan]Updating..",
                                total=100, style="bar")
                            for i in range(300):
                                time.sleep(0.01)
                                progress.update(task, advance=1)

                            progress.update(task, completed=100, complete_style="complete")

                        panel_choice = Panel(
                            Text("Customer Information Changed Successfully!", justify="center", style="bold bright_cyan"),
                            title="UPDATE!",
                            border_style="bold green",
                        )
                        rprint(panel_choice)
                else:
                    panel_choice = Panel(
                        Text("ID Number Cannot contain any letter, will stay with previous ID number ", justify="center", style="bold bright_cyan"),
                        title="UPDATE!",
                        border_style="bold green",
                    )
                    rprint(panel_choice)


            else:
                panel_choice = Panel(
                    Text("Customer age cannot contain any letter", justify="center", style="bold bright_cyan"),
                    title="UPDATE!",
                    border_style="bold green",
                )
                rprint(panel_choice)

        else:
            panel_choice = Panel(
                Text("Customer does not exist", justify="center", style="bold bright_cyan"),
                title="UPDATE!",
                border_style="bold green",
            )
            rprint(panel_choice)
    else:
        panel_choice = Panel(
            Text("ID Number Should not Contain any letter ", justify="center", style="bold bright_cyan"),
            title="UPDATE!",
            border_style="bold green",
        )
        rprint(panel_choice)

def UpdateCar():
    id = input(
        "                                                                                                         Type ID Number to Update: ")
    if id.isdigit():
        id = int(id)
        if id in CarID:
            i = CarID.index(id)
            cname = Panel(
                Text(f"Enter New Car Brand for {CarBrand[i]}", justify="center", style="bold bright_cyan"),
                title="UPDATE!",
                border_style="bold green",
            )
            rprint(cname)
            CarBrand[i] = input(
                f"                                                                                         ")
            cname = Panel(
                Text(f"Enter New Car Model for {CarModel[i]}", justify="center", style="bold bright_cyan"),
                title="UPDATE!",
                border_style="bold green",
            )
            rprint(cname)
            CarModel[i] = input(
                f"                                                                                         ")
            cname = Panel(
                Text(f"Enter New Car Type for {CarType[i]}", justify="center", style="bold bright_cyan"),
                title="UPDATE!",
                border_style="bold green",
            )
            rprint(cname)
            CarType[i] = input(
                f"                                                                                         ")
            cname = Panel(
                Text(f"Enter New Car ID for {CarID[i]}", justify="center", style="bold bright_cyan"),
                title="UPDATE!",
                border_style="bold green",
            )
            rprint(cname)
            carid = input(
                f"                                                                                         ")
            if carid.isdigit():
                carid = int(carid)
                if carid in CarID:
                    cname = Panel(
                        Text(f"The Car ID Already Exists! Will stay with previous Car ID", justify="center", style="bold bright_cyan"),
                        title="UPDATE!",
                        border_style="bold green",
                    )
                    rprint(cname)
                else:
                    CarID[i] = int(carid)



                    cname = Panel(
                        Text(f"Enter New Car Price for {CarPrice[i]}", justify="center", style="bold bright_cyan"),
                        title="UPDATE!",
                        border_style="bold green",
                    )
                    rprint(cname)
                    carprice = input(
                        f"                                                                                         ")

                    if carprice.isdigit():
                        CarPrice[i] = int(carprice)

                        with Progress() as progress:
                            task = progress.add_task(
                                "                                                                                        [cyan]Updating..",
                                total=100, style="bar")
                            for i in range(300):
                                time.sleep(0.01)
                                progress.update(task, advance=1)

                            progress.update(task, completed=100, complete_style="complete")

                        panel_choice = Panel(
                            Text("Car Information Changed Successfully!", justify="center", style="bold bright_cyan"),
                            title="UPDATE!",
                            border_style="bold green",
                        )
                        rprint(panel_choice)
                    else:
                        panel_choice = Panel(
                            Text("Car Price Cannot Contain Any Letters", justify="center", style="bold bright_cyan"),
                            title="UPDATE!",
                            border_style="bold green",
                        )
                        rprint(panel_choice)
            else:
                panel_choice = Panel(
                    Text("Car ID Cannot Contain Any Letter", justify="center", style="bold bright_cyan"),
                    title="UPDATE!",
                    border_style="bold green",
                )
                rprint(panel_choice)
        else:
            panel_choice = Panel(
                Text("CAR DOES NOT EXIST!", justify="center", style="bold bright_cyan"),
                title="UPDATE!",
                border_style="bold green",
            )
            rprint(panel_choice)

def SearchCustomer():
    search = input(
        "                                                                             Type Customer Details to Search: ").strip().lower()
    panel_choice = Panel(
        Text(f"{search}", justify="center", style="bold bright_cyan"),
        title="SEARCHING",
        border_style="bold green",
    )

    rprint(panel_choice)

    found_customers= False

    table = Table(title="SEARCH RESULTS", title_justify="center", width=230)
    table.add_column("Name", justify="center", style="cyan")
    table.add_column("Age", justify="center", style="red")
    table.add_column("Gender", justify="center", style="green")
    table.add_column("ID Type", justify="center", style="blue")
    table.add_column("ID Number", justify="center", style="yellow")

    table.add_column("Car Brand Rented", justify="center", style="cyan")
    table.add_column("Car ID Rented", justify="center", style="blue")
    table.add_column("Car Model Rented", justify="center", style="red")
    table.add_column("Car Type Rented", justify="center", style="green")
    table.add_column("Car Rented Price", justify="center", style="yellow")
    table.add_column("Days Rented", justify="center", style="blue")

    for i in range(len(CustomerName)):

        if(
        search in str(IDNumber[i]).lower()
        or search in CustomerName[i].lower()
        or search in CustomerGender[i].lower()
        or search in str(CustomerAge[i]).lower()
        or search in IDType[i].lower()
        ):

            table.add_row(
                CustomerName[i],
                str(CustomerAge[i]),
                CustomerGender[i],
                IDType[i],
                str(IDNumber[i]),
                str(RentedCarBrand[i]),
                str(RentedCarID[i]),
                str(RentedCarModel[i]),
                str(RentedCarType[i]),
                str(RentedCarPrice[i]),
                str(RentedDays[i]),)
            found_customers = True

    rprint(table)



    if not found_customers:
        panel_choice = Panel(
                    Text("CUSTOMER NOT FOUND", justify="center", style="bold bright_cyan"),
                    title="UPDATE!",
                    border_style="bold green",
                )
        rprint(panel_choice)


def SearchCars():


    search_query = input("                                                                                  Type Car Details to Search: ").strip().lower()
    panel_choice = Panel(
        Text(f"{search_query}", justify="center", style="bold bright_cyan"),
        title="SEARCHING",
        border_style="bold green",
    )
    rprint(panel_choice)

    found_cars = False
    table1 = Table(title="Car List", title_justify="center", width=230)
    table1.add_column("Car ID", justify="center", style="magenta")
    table1.add_column("Car Brand", justify="center", style="cyan")
    table1.add_column("Car Model", justify="center", style="red")
    table1.add_column("Car Type", justify="center", style="green")
    table1.add_column("Car Price", justify="center", style="blue")

    for i in range(len(CarID)):
        if (
                search_query in str(CarID[i]).lower()
                or search_query in CarBrand[i].lower()
                or search_query in CarModel[i].lower()
                or search_query in CarType[i].lower()
        ):
            table1.add_row(str(CarID[i]), CarBrand[i], CarModel[i], CarType[i], str(CarPrice[i]))



            found_cars = True
    rprint(table1)



    if not found_cars:
        panel_choice = Panel(
            Text("NO CARS FOUND", justify="center", style="bold bright_cyan"),
            title="UPDATE!",
            border_style="bold green",
        )
        rprint(panel_choice)

def ShowEarnings():

    message = Text(f"Our Total Earnings Are: ₱{earnings}  ")
    welcome_message = Panel(Text(f"{message}", justify="center", style="bold bright_cyan"), title="RENT-A-RIDE",
                            border_style="bold green")
    rprint(welcome_message)

welcomefunction()
choosemenu()

