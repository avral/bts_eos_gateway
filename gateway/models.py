from django.db import models


class Transfer(models.Model):
    amount = models.DecimalField('Currency Amount',
                                 default=0,
                                 null=True,
                                 max_digits=19,
                                 decimal_places=10)

    eos_name = models.CharField(max_length=100, null=True)
    eos_hash = models.CharField(max_length=100, null=True)
    bts_name = models.CharField(max_length=100, null=True)

    processed_at = models.DateTimeField(auto_now_add=True)
    tokens_emitted = models.BooleanField('Tokens are emitted', default=False)
    sys_message = models.TextField()

    block_num = models.IntegerField(null=True)
    is_valid_memo = models.BooleanField(default=True)

    def __str__(self):
        return f'{self.amount} | {self.bts_name} -> {self.eos_name}'
