[SQL: 
CREATE TABLE paymentrequest (
        author UUID NOT NULL, 
        type_id INTEGER NOT NULL, 
        payer_id INTEGER NOT NULL, 
        recipient_id INTEGER NOT NULL, 
        created_on TIMESTAMP WITHOUT TIME ZONE DEFAULT CURRENT_TIMESTAMP NOT NULL, 
        updated_on TIMESTAMP WITHOUT TIME ZONE DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP NOT NULL, 
        kfp_id INTEGER, 
        due_date TIMESTAMP WITHOUT TIME ZONE, 
        purpose VARCHAR(210), 
        amount_netto FLOAT, 
        amount_vat FLOAT, 
        amount_total FLOAT, 
        attach_url VARCHAR(150), 
        field_101_id INTEGER, 
        field_104_id INTEGER, 
        field_105_id INTEGER, 
        field_106 VARCHAR(20), 
        field_107 VARCHAR(20), 
        field_108 VARCHAR(20), 
        field_109 VARCHAR(20), 
        project VARCHAR(50), 
        contract VARCHAR(50), 
        contract_date TIMESTAMP WITHOUT TIME ZONE, 
        sub_contract VARCHAR(50), 
        sub_contract_date TIMESTAMP WITHOUT TIME ZONE, 
        prepayment_id INTEGER, 
        id SERIAL NOT NULL, 
        description VARCHAR(150), 
        PRIMARY KEY (id), 
        FOREIGN KEY(author) REFERENCES "user" (id), 
        FOREIGN KEY(field_101_id) REFERENCES payerstatus (id), 
        FOREIGN KEY(field_104_id) REFERENCES kbk (id), 
        FOREIGN KEY(field_105_id) REFERENCES oktmo (id), 
        FOREIGN KEY(kfp_id) REFERENCES kfp (id), 
        FOREIGN KEY(payer_id) REFERENCES payer (id), 
        FOREIGN KEY(prepayment_id) REFERENCES prepayment (id), 
        FOREIGN KEY(recipient_id) REFERENCES counteragent (id), 
        FOREIGN KEY(type_id) REFERENCES paymenttype (id)
)

]