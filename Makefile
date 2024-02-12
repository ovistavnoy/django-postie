test-requirements:
	pipenv lock -d -r > requirements.txt
	pipenv lock -r >> requirements.txt

