# Dependency notes

This document lists the reasons why specific dependencies are pinned down to
exact versions. Make sure to consider these points before updating dependencies
to their latest versions.

## `jsonschema`

### macOS build

On macOS, `jsonschema >= 4.20` is required as older versions seem to have
problems in the bundled executable version with loading the schemas.

### Other platforms

For sake of simplicitly, other platforms should be consistent with the macOS
build, i.e. `jsonschema >= 4.20` should be used.
