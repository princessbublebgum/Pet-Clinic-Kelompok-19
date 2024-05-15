class ClinicInvoice:
    def __init__(self, client_name):
        self.client_name = client_name
        self.services = []

    def add_service(self, service_name, service_cost):
        self.services.append({"name": service_name, "cost": service_cost})

    def calculate_total(self):
        return sum(service["cost"] for service in self.services)

    def print_invoice(self):
        print("Clinic Invoice")
        print("===================")
        print(f"Client Name: {self.client_name}")
        print("-------------------")
        
        for service in self.services:
            print(f"{service['name']}: Rp{service['cost']:.2f}")
        
        total_cost = self.calculate_total()
        print("-------------------")
        print(f"Total Cost: Rp{total_cost:.2f}")
        print("===================")

# Fungsi untuk menjalankan program dan mengambil input dari pengguna
def main():
    client_name = input("Enter appointment name: ")
    invoice = ClinicInvoice(client_name)

    while True:
        service_name = input("Enter service name (or 'done' to finish): ")
        if service_name.lower() == 'done':
            break
        service_cost = float(input(f"Enter cost for {service_name}: "))
        invoice.add_service(service_name, service_cost)

    invoice.print_invoice()

if __name__ == "__main__":
    main()
