#!/bin/bash

# Generate SDK

PACKAGE_VERSION="$1"

docker run --rm \
  -v "${PWD}":/local openapitools/openapi-generator-cli generate \
  --input-spec https://api.opendota.com/api \
  --generator-name python \
  --template-dir /local/custom-template \
  --ignore-file-override /local/.openapi-generator-ignore \
  --global-property=apiTests=false,modelTests=false \
  --config /local/config.yml \
  --additional-properties=packageVersion="$PACKAGE_VERSION" \
  --output /local