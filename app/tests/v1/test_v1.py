sys:1: SAWarning: relationship 'PaymentStatus.paymentregister' will copy column paymentstatus.id to column paymentregister.status_id, which conflicts with relationship(s):
      'PaymentRegister.paymentstatid to paymentregister.status_id), 
      'PaymentStatus.register' (copies paymentstatus.id to paymentregister.status_id).
      If this is not the intention, consider if these relationships should be linked with bnly=True should be applied to one or more if they are read-only.
      For the less common case that foreign key constraints are partially overlapping, the orm.foreign() annotation can be used to isolate thritten towards.
      To silence this warning, add the parameter 'overlaps="paymentstatus,register"' to the 'PaymentStatus.paymentregister' relationship.
      (Background on this error at: https://sqlalche.me/riginated from the `configure_mappers()` process, which was invoked automatically in response to a user-initiated operation.)
sys:1: SAWarning: relationship 'PaymentRegister.status' will copy column paymentstatus.id to column paymentregister.status_id, which conflicts with relationship(s):
        'PaymentRegister.paymentstatus' (coaymentregister.status_id), 'PaymentStatus.register' (copies paymentstatus.id to paymentregister.status_id).
        If this is not the intention, consider if these relationships should be linked with back_pope should be applied to one or more if they are read-only.
        For the less common case that foreign key constraints are partially overlapping, the orm.foreign() annotation can be used to isolate the colum towards.
        To silence this warning, add the parameter 'overlaps="paymentstatus,register"' to the 'PaymentRegister.status' relationship.
        (Background on this error at: https://sqlalche.me/e/20/qzyx) (Th the `configure_mappers()` process, which was invoked automatically in response to a user-initiated operation.)
