def driving_cost(miles_per_gallon, dollars_per_gallon, miles_driven):
   
   dollars_per_mile = dollars_per_gallon/miles_per_gallon
   dollars = dollars_per_mile*miles_driven
   return dollars

if __name__ == '__main__':
    miles_per_gallon = float(input())
    dollars_per_gallon = float(input())
    #print your costs here like example below
    print(f'{driving_cost(miles_per_gallon, dollars_per_gallon, 10.0):.2f}')
    print(f'{driving_cost(miles_per_gallon, dollars_per_gallon, 50.0):.2f}')
    print(f'{driving_cost(miles_per_gallon, dollars_per_gallon, 400.0):.2f}')
   