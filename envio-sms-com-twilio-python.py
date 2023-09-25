from twilio.rest import Client

# Suas credenciais do Twilio
account_sid = "seu_account_sid"
auth_token = "seu_auth_token"

# Número de telefone remetente do Twilio (deve ser registrado no Twilio e verificado)
sender_phone_number = "+123456789"

# Número de telefone de destino (para onde você deseja enviar a mensagem SMS)
recipient_phone_number = "+123456789"

# Mensagem que deseja enviar
mensagem = "PARABÉNS!!! VOCÊ GANHOU 1 MILHÃO DE BEIJOS!!! POR SER A MELHOR ESPOSA E A MELHOR MÃE DO MUNDOO!!! S2   TE AMO!   ASS:Douglas"

def enviar_mensagem_sms(numero_destino, mensagem):
    try:
        # Inicializa o cliente Twilio
        client = Client(account_sid, auth_token)

        # Envia a mensagem SMS
        message = client.messages.create(
            body=mensagem,
            from_=sender_phone_number,
            to=numero_destino
        )

        print(f'Mensagem SMS enviada para {numero_destino}: "{mensagem}"')
        print(f'SID da mensagem: {message.sid}')
    except Exception as e:
        print(f'Erro ao enviar mensagem SMS: {str(e)}')

if __name__ == "__main__":
    enviar_mensagem_sms(recipient_phone_number, mensagem)

