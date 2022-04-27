#!/bin/bash

# Remove unused files from general python template (https://github.com/OpenAPITools/openapi-generator/tree/master/modules/openapi-generator/src/main/resources/python)

TEMPLATE_IGNORE_FILES='.ignore-template-files'
OPENAPI_GENERATOR_FILES='.openapi-generator/FILES'

# read 'ignore template files' by lines
while read line; do
  case "$line" in \#*) continue ;; esac # skip comment lines

  sed -i "/$line/d" $OPENAPI_GENERATOR_FILES # modify openapi generator file list
  rm -f "$line"
done < $TEMPLATE_IGNORE_FILES
