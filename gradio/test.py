from gradio_client import Client

client = Client("http://127.0.0.1:7860/")
result = client.predict(
				"Howddasdasdasasdsay!",	# str representing input in 'name' Textbox component
				api_name="/predict"
)
print(result)