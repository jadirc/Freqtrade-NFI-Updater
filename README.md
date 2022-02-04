# Freqtrade NFI Updater

This code allows you to run the Freqtrade trading bot while using the NostalgiaForInfinity strategy.
The code allows a daily update of this strategy and has an easy setup.

## Prerequisites

Make sure you have the following tools installed:
- Docker
- Docker-compose

## Setup

### Installing the project

Open a terminal window and clone this repository to your machine by executing the following line.

```bash
git@github.com:thomastunc/Freqtrade-NFI-Updater.git
```

Then, cd to the folder.

```bash
cd Freqtrade-NFI-Updater
```

### Updating variables

Copy the ```.env.dist``` file to an ```.env``` file with the following command.

```bash
cp .env.dist .env
```

Alter the values for the variables in the ```.env``` to the ones that correspond to your needs.
You can do this with a text editor or by using nano.

```bash
nano .env
```

## Usage

Everything runs through Docker, so after changing the variables you only need to run:

```bash
docker-compose up -d
```