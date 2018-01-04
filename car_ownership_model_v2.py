# -*- coding: utf-8 -*-
"""
Created on Thu Jan  4 11:36:07 2018

@author: fculfaz
"""

""" example inputs below
make = "Audi"
model = "A3"
purchase_cost	 = 19000
deposit = 5000
years_to_pay = 4
interest = 1.04
depreciation_factor_per_year =	0.9
mileage_per_year = 10000
fuel_economy = 50 #mpg
gallon = 4.55 #litres
price_per_litre = 1.22
yearly_insurance = 200
yearly_MOT =	40
yearly_tax =	130
service_every = 12000 #miles
per_service_cost = 300 
years_driven = 5
other_maintenence_per_year = 200
other_yearly_parking_fines_etc = 150

"""

def cost(make,model,purchase_cost,deposit,years_to_pay,interest,depreciation_factor_per_year,mileage_per_year,fuel_economy,price_per_litre,yearly_insurance,yearly_MOT,yearly_tax,service_every,per_service_cost,years_driven,other_maintenence_per_year,other_yearly_parking_fines_etc):
    print("Inputs:")
    print("Make: ",make)
    print("Model: ",model)
    print("Purchase Cost = ", purchase_cost)
    print("Deposit = ",deposit)
    print("Years to pay off the car = ",years_to_pay)
    print("Interest =",interest)
    print("Depreciation factor = ",depreciation_factor_per_year)
    print("Mileage per year (miles) =",mileage_per_year)
    print("Fule ecomomy (mpg) =",fuel_economy)
    print("Fuel price (/l) = ",price_per_litre)
    print("Yearly Insurance =",yearly_insurance)
    print("MOT (/year) =",yearly_MOT)
    print("TAX(/year) ",yearly_tax)
    print("Service every",service_every," miles")
    print("Service cost (/year) =",per_service_cost)
    print("Years driven =",years_driven)
    print("Other maintenance costs (/year) =",other_maintenence_per_year)
    print("Other costs like parking fines and traffuc offences (/year) =",other_yearly_parking_fines_etc)
    
    print("Calculations:")
    monthly_payments = ((purchase_cost-deposit)*interest)/(years_to_pay*12)
    print("Monthly Payments =",monthly_payments)
    yearly_spend_fuel	 = (mileage_per_year/fuel_economy)*gallon*price_per_litre
    total_lifetime_service_cost =  ((mileage_per_year*years_driven)/service_every)*per_service_cost
    print("Total lifetime service cost =",total_lifetime_service_cost)                               
    total_value_of_car_at_end = purchase_cost*(depreciation_factor_per_year**years_driven)
    print("Total Value of Car at the end =",total_value_of_car_at_end)
    total_spend_running_costs = (yearly_insurance*years_driven)+(yearly_MOT*years_driven)+total_lifetime_service_cost+(other_maintenence_per_year*years_driven)+(yearly_tax*years_driven)+(yearly_spend_fuel*years_driven)+(other_yearly_parking_fines_etc*years_driven)
    print("Total spend including running costs =",total_spend_running_costs)
    yearly_running_costs	= total_spend_running_costs/years_driven
    print("Yearly running costs =",yearly_running_costs)
    yearly_running_costs_inc_car_purchase	= yearly_running_costs+((purchase_cost-deposit)/years_driven)
    print("Yearly running costs including car purchase =",yearly_running_costs_inc_car_purchase)
    real_total_spend = ((purchase_cost*interest)+total_spend_running_costs)-total_value_of_car_at_end
    print("Real total spend =",real_total_spend)
    