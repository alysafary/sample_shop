from django.db import models


class Product(models.Model):
    productCode = models.CharField(max_length=15, primary_key=True)
    productName = models.CharField(max_length=70)
    productScale = models.CharField(max_length=10)
    productVendor = models.CharField(max_length=50)
    productDescription = models.TextField()
    quantityInStock = models.SmallIntegerField()
    buyPrice = models.DecimalField(max_digits=10, decimal_places=2)
    MSRP = models.DecimalField(max_digits=10, decimal_places=2)


class Employee(models.Model):
    employeeNumber = models.IntegerField(primary_key=True)
    lastName = models.CharField(max_length=50)
    firstName = models.CharField(max_length=50)
    extension = models.CharField(max_length=10)
    email = models.EmailField()
    reportsTo = models.ForeignKey('self', on_delete=models.CASCADE, null=True)
    jobTitle = models.CharField(max_length=50)


class Customer(models.Model):
    customerNumber = models.IntegerField(primary_key=True)
    customerName = models.CharField(max_length=50)
    contactLastName = models.CharField(max_length=50)
    contactFirstName = models.CharField(max_length=50)
    phone = models.CharField(max_length=50)
    addressLine1 = models.CharField(max_length=50)
    addressLine2 = models.CharField(max_length=50, blank=True, null=True)
    city = models.CharField(max_length=50)
    state = models.CharField(max_length=50, blank=True, null=True)
    postalCode = models.CharField(max_length=15, blank=True, null=True)
    country = models.CharField(max_length=50)
    salesRepEmployeeNumber = models.ForeignKey(
        Employee, on_delete=models.CASCADE, null=True)
    creditLimit = models.DecimalField(
        max_digits=10, decimal_places=2, null=True)


class Payment(models.Model):
    customerNumber = models.ForeignKey(Customer, on_delete=models.CASCADE)
    checkNumber = models.CharField(max_length=50)
    paymentDate = models.DateField()
    amount = models.DecimalField(max_digits=10, decimal_places=2)


class Order(models.Model):
    orderNumber = models.IntegerField(primary_key=True)
    orderDate = models.DateField()
    requiredDate = models.DateField()
    shippedDate = models.DateField(null=True, blank=True)
    status = models.CharField(max_length=15)
    comments = models.TextField()
    customerNumber = models.ForeignKey(Customer, on_delete=models.CASCADE)


class OrderDetail(models.Model):
    orderNumber = models.ForeignKey(Order, on_delete=models.CASCADE)
    productCode = models.ForeignKey(Product, on_delete=models.CASCADE)
    quantityOrdered = models.IntegerField()
    priceEach = models.DecimalField(max_digits=10, decimal_places=2)
    orderLineNumber = models.SmallIntegerField()
