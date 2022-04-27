#!/bin/bash

# Find difference between OpenAPI specifications

OLD_SPEC="$1"
NEW_SPEC="$2"

docker run --rm -v "$(pwd):/specs:ro" openapitools/openapi-diff:2.0.1 "$OLD_SPEC" "$NEW_SPEC" --markdown changes.md
