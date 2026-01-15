# Changelog

## [1.1.1](https://github.com/NASA-ACROSS/across-server-openapi-python/compare/v1.1.0...v1.1.1) (2026-01-15)


### Bug Fixes

* refresh before `param_serialize` so token is set for call ([#27](https://github.com/NASA-ACROSS/across-server-openapi-python/issues/27)) ([e41a86b](https://github.com/NASA-ACROSS/across-server-openapi-python/commit/e41a86b989e54681352e65a4c0606b97bce24107))
* refresh before param_serialize so token is set for call ([e41a86b](https://github.com/NASA-ACROSS/across-server-openapi-python/commit/e41a86b989e54681352e65a4c0606b97bce24107))

## [1.1.0](https://github.com/NASA-ACROSS/across-server-openapi-python/compare/v1.0.0...v1.1.0) (2026-01-09)


### Features

* **actions:** Adding publish to pypi workflow ([#20](https://github.com/NASA-ACROSS/across-server-openapi-python/issues/20)) ([a0a0c23](https://github.com/NASA-ACROSS/across-server-openapi-python/commit/a0a0c2385f672b961f60186ba819b1f2b4d35753))
* **actions:** adding release-please workflow action to ci/cd ([#22](https://github.com/NASA-ACROSS/across-server-openapi-python/issues/22)) ([186365b](https://github.com/NASA-ACROSS/across-server-openapi-python/commit/186365bc84cd19d789a36bf6296e45e36af515cf))
* add client wrapper ([ec307c6](https://github.com/NASA-ACROSS/across-server-openapi-python/commit/ec307c6e85fc61eecda47ecf597cb321f28ed601))
* add client wrapper ([2eb2d89](https://github.com/NASA-ACROSS/across-server-openapi-python/commit/2eb2d893c3d5a3c591990d95c2344871104c3147))
* add manual-update-instructions.md ([b925ff2](https://github.com/NASA-ACROSS/across-server-openapi-python/commit/b925ff2574aa506fde45e663cc70c8704f5cd46d))
* add manual-update-instructions.md ([88e5053](https://github.com/NASA-ACROSS/across-server-openapi-python/commit/88e505310a4e544ae75a4a0b1f5654380b8f6cee))
* generated sdk client ([d531116](https://github.com/NASA-ACROSS/across-server-openapi-python/commit/d531116c9719854783fea15c5065213297ffbad0))
* **legal:** add NASA copyright notices ([3ff63f3](https://github.com/NASA-ACROSS/across-server-openapi-python/commit/3ff63f385a0597023ee8793d4056c0d915205468))
* **legal:** add NASA copyright notices ([96a9925](https://github.com/NASA-ACROSS/across-server-openapi-python/commit/96a99253318e1831ee193551b1ef336644d8ca12))
* update openapi sdk with across-server 1.1.0 ([038faa3](https://github.com/NASA-ACROSS/across-server-openapi-python/commit/038faa3b85020da79d91fb978abaaf0abf60f8ad))
* update sdk ([ba45dfc](https://github.com/NASA-ACROSS/across-server-openapi-python/commit/ba45dfc8c7542192366678c3df4b79ed74253e0c))
* update sdk to latest dev c1360e0 ([c468329](https://github.com/NASA-ACROSS/across-server-openapi-python/commit/c468329f597e60525e65cb2ebeeef7a67cd19372))


### Bug Fixes

* add debug logs for key rotation ([#23](https://github.com/NASA-ACROSS/across-server-openapi-python/issues/23)) ([2bda8c5](https://github.com/NASA-ACROSS/across-server-openapi-python/commit/2bda8c5b04d0415065b5f730874931959d366fd7))
* attempt refresh and retry when credentials exist ([ede2b76](https://github.com/NASA-ACROSS/across-server-openapi-python/commit/ede2b76a10a5d364eeaa90182a1a77fbad639944))
* check jwt is a str, don't refresh access token for get methods ([6716c3a](https://github.com/NASA-ACROSS/across-server-openapi-python/commit/6716c3ae2e16ec0cefee5b166f0df03e3f76871d))
* detect access token expiration and refresh access token when close to expired ([872a1ac](https://github.com/NASA-ACROSS/across-server-openapi-python/commit/872a1ac328b8a5b19fee8ed968b120412723f903))
* detect access token expiration and refresh access token when close to expired ([#6](https://github.com/NASA-ACROSS/across-server-openapi-python/issues/6)) ([4d1e99d](https://github.com/NASA-ACROSS/across-server-openapi-python/commit/4d1e99d2863c7cdead48150836f5f631e1cbc3ca))
* don't refresh access token for get methods ([b775a75](https://github.com/NASA-ACROSS/across-server-openapi-python/commit/b775a759b253dffad3dafba6981c68ba50e287c4))
* **legal:** remove extra line ([95cd601](https://github.com/NASA-ACROSS/across-server-openapi-python/commit/95cd6011b06a69b177d369e25f0b7952fdbd868f))
* **license:** update to apache-2.0 license ([7da09c3](https://github.com/NASA-ACROSS/across-server-openapi-python/commit/7da09c33ca6659281eae3ae62ad2a9449c912b87))
* **license:** update to apache-2.0 license ([30cd126](https://github.com/NASA-ACROSS/across-server-openapi-python/commit/30cd126be5f6b292013fde7a942c91492bc14231))
* minor changes to trigger workflows ([#24](https://github.com/NASA-ACROSS/across-server-openapi-python/issues/24)) ([afcbdf5](https://github.com/NASA-ACROSS/across-server-openapi-python/commit/afcbdf5ab3f0004fbf64140411522195c4b9bcb9))
* **namespace:** add code to fix namespace issue due to boilerplate ([#18](https://github.com/NASA-ACROSS/across-server-openapi-python/issues/18)) ([5bdd554](https://github.com/NASA-ACROSS/across-server-openapi-python/commit/5bdd5543c99228f1d2d282df5c7ca47ee8a5fde1))
* NASA-ACROSS ([5f8b17d](https://github.com/NASA-ACROSS/across-server-openapi-python/commit/5f8b17d8467e4fb2f4852b2306bcfc4b119301e9))
* **org-name:** update organization name ([98f8da8](https://github.com/NASA-ACROSS/across-server-openapi-python/commit/98f8da83e8900b2e13088c065087a5a442b6b560))
* **org-name:** update organization name ([a13c275](https://github.com/NASA-ACROSS/across-server-openapi-python/commit/a13c27545372ef975e6b1ccc77d5ffcf0b03424d))
* return converted dt with tzinfo for token exp ([9e38e92](https://github.com/NASA-ACROSS/across-server-openapi-python/commit/9e38e9255a919818364010ab8aea97bb542aa9fd))
* run release-please ([40c1f0d](https://github.com/NASA-ACROSS/across-server-openapi-python/commit/40c1f0db9a37bdcb08ffa88c47188e4ad785f4e6))
* update sdk ([ada5da6](https://github.com/NASA-ACROSS/across-server-openapi-python/commit/ada5da6842ffce67eb5f8755b880e008f004c1db))
