from django.contrib import admin
from .models import *

class ExpenseCategoryAdmin(admin.ModelAdmin):
    list_display = ('name', 'type', 'creation_date')

class IncomeCategoryAdmin(admin.ModelAdmin):
    list_display = ('name', 'creation_date')

class WalletAdmin(admin.ModelAdmin):
    list_display = ('name', 'type', 'creation_date')

class ExpenseAdmin(admin.ModelAdmin):
    list_display = ('concept', 'qty', 'category', 'wallet', 'expense_date' , 'creation_date')

class IncomeAdmin(admin.ModelAdmin):
    list_display = ('concept', 'qty', 'category', 'wallet', 'income_date' , 'creation_date')

class TotalAdmin(admin.ModelAdmin):
    list_display = ('wallet', 'qty', 'update_date')

admin.site.register(ExpenseCategory, ExpenseCategoryAdmin)
admin.site.register(IncomeCategory, IncomeCategoryAdmin)
admin.site.register(Wallet, WalletAdmin)
admin.site.register(Expense, ExpenseAdmin)
admin.site.register(Income, IncomeAdmin)
admin.site.register(Total, TotalAdmin)