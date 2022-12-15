# Fractional Attribution Accelerator
This accelerator guides the user through how to set-up and run fractional attribution analysis on Snowplow data, coined 'Fractribution'.

## Installation

Recursively update the git submodules:

```sh
git submodule update --init --recursive
```

To build the Hugo app:

```sh
./scripts/build.sh build
```

## Usage

To start an HTTP server serving the app, use:

```sh
./scripts/build.sh serve
```

This will run `hugo server` on the background.