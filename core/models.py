from django.db import models

class ExpenseCategory(models.Model):
    
    name = models.CharField(max_length=50)

    FIXED = 'Fixed'
    VARIABLE = 'Variable'

    TYPE_CHOICES = [
        (FIXED, 'Fixed'),
        (VARIABLE, 'Variable'),
    ]

    type = models.CharField(max_length=10, choices=TYPE_CHOICES)

    creation_date = models.DateTimeField(
        auto_now_add=True, 
        blank=True,
    )

    class Meta:    
        verbose_name_plural = "expense categories" 
        unique_together = [['name']]

    def __str__(self):
        return self.name

class IncomeCategory(models.Model):
    
    name = models.CharField(max_length=50)

    creation_date = models.DateTimeField(
        auto_now_add=True, 
        blank=True,
    )

    class Meta:    
        verbose_name_plural = "income categories"
        unique_together = [['name']]

    def __str__(self):
        return self.name

class Wallet(models.Model):

    name = models.CharField(max_length=50)

    DEBIT = 'Debit Card'
    CASH = 'Cash'
    VOUCHER = 'Pantry Voucher'
    CREDIT = 'Credit Card'
    LOAN = 'Loan'

    TYPE_CHOICES = [
        (DEBIT, 'Debit Card'),
        (CASH, 'Cash'),
        (VOUCHER, 'Pantry Voucher'),
        (CREDIT, 'Credit Card'),
        (LOAN, 'Loan'),
    ]

    type = models.CharField(max_length=15, choices=TYPE_CHOICES)

    creation_date = models.DateTimeField(
        auto_now_add=True, 
        blank=True,
    )

    class Meta:    
        unique_together = [['name']]

    def __str__(self):
        return self.name

class Expense(models.Model):

    concept = models.CharField(max_length=50)

    qty = models.IntegerField()

    category = models.ForeignKey(ExpenseCategory, on_delete=models.CASCADE)

    wallet = models.ForeignKey(Wallet, on_delete=models.CASCADE)

    expense_date = models.DateTimeField()

    creation_date = models.DateTimeField(
        auto_now_add=True, 
        blank=True,
    )

    def __str__(self):
        return self.concept
    
    @property
    def Sum_Expense(self):
        sum_exp = self.qty + sum
        return sum_exp

class Income(models.Model):

    concept = models.CharField(max_length=50)

    qty = models.IntegerField()

    category = models.ForeignKey(IncomeCategory, on_delete=models.CASCADE)

    wallet = models.ForeignKey(Wallet, on_delete=models.CASCADE)

    income_date = models.DateTimeField()

    creation_date = models.DateTimeField(
        auto_now_add=True, 
        blank=True,
    )

    def __str__(self):
        return self.concept
    
    @property
    def Sum_Income(self):
        sum_inc =+ self.qty
        return sum_inc

class Total(models.Model):

    wallet = models.ForeignKey(Wallet, on_delete=models.CASCADE)

    qty = models.IntegerField()

    update_date = models.DateTimeField(
        auto_now_add=True, 
        blank=True,
    )

    def __str__(self):
        return f"{self.wallet}: {self.qty}"
    
    @property
    def Sum_Total(self):
        sum_tot = Income.Sum_Income - Expense.Sum_Expense
        return sum_tot