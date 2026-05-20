sdk: ## Generate sdk client
	@docker run --rm \
		-v ${PWD}:/local \
			openapitools/openapi-generator-cli:v7.14.0 generate \
		-i /local/openapi.json \
		-g python \
		-o /local/. \
		-c /local/openapi-config.json \
		--global-property generateApiTests=false,generateModelTests=false \
		--package-name across.sdk.v1