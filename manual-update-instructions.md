# Manually updating the SDK

1. Pull the across-server repo 
2. Checkout the branch/sha you'd like to update this SDK to
3. Write down the short commit sha (example: `c76e494`)
4. Run across-server locally (follow instructions in readme `make dev`)
5. Visit api docs and load the [`openapi.json`](http://localhost:8000/api/v1/openapi.json) (make sure it's the api/v1/ version)
6. create a `openapi.json` in the root of across-server-openapi-python repo and save (it should be gitignored)
7. run `make sdk` in across-server-openapi-python repo
8. commit the update to main with the commit sha from step 2  
    `feat: update sdk to latest c76e494`
9. Pull dependent repo (across-client or across-data-ingestion)
10. run `make lock`
11. commit the lock changes to the dependent repo