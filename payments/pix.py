import uuid
import qrcode

class Pix:
    def __init__(self):
        pass
    
    def create_payment(self):
        # simula um codigo de pagamento de uma instituição financeira
        bank_payment_id = str(uuid.uuid4())

        # simula a geração de um codigo copia e cola
        hash_payment = f'has_payment_{bank_payment_id}'

        # geração de um qr code
        img = qrcode.make(hash_payment)

        # salva a imagem do qrcode como arquivo PNG
        img.save(f"static/img/qr_code_payment_{bank_payment_id}.png")
        
        return {"bank_payment_id": bank_payment_id,
                "qr_code_path": f"qr_code_payment_{bank_payment_id}"}