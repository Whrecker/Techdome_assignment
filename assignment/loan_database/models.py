from django.db import models
class Admin(models.Model):
	ids=models.IntegerField(primary_key=True)
	name=models.CharField(max_length=100)
	password = models.CharField(max_length=100)

class Customers(models.Model):

	ids=models.IntegerField(primary_key=True)
	username=models.CharField(max_length=100)
	password = models.CharField(max_length=100)
	loan_taken=models.IntegerField()
	loan_remaining=models.IntegerField()
	repayment_time=models.DateTimeField(null=True)
	loan_status=models.CharField(max_length=20)
	loan_term=models.IntegerField(null=True)

	def get_special_combination_value(self):
		return '{}{}{}{}{}{}'.format(username,password,loan_taken,loan_remaining,repayment_time,loan_status)
	def __str__(self):
		return self.username