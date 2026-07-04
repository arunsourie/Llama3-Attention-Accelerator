# Day 03 - Vivado Environment and Zynq UltraScale+ Architecture

**Date:** 04 July 2026

---

# Objective

Understand the FPGA development environment, the Zynq UltraScale+ MPSoC architecture, and prepare the hardware platform for future accelerator development.

---

# Topics Studied

- FPGA Basics
- CPU vs FPGA
- Zynq UltraScale+ MPSoC
- Processing System (PS)
- Programmable Logic (PL)
- ZCU102 Development Board
- Vivado Design Suite
- Block Design
- Hardware Platform Export (.xsa)

---

# Concepts Learned

## FPGA

A Field Programmable Gate Array (FPGA) is a programmable hardware device that allows custom digital circuits to be implemented after manufacturing.

Unlike CPUs, FPGAs execute many operations in parallel by implementing hardware directly.

---

## CPU vs FPGA

CPU executes software instructions sequentially.

FPGA implements hardware circuits capable of parallel computation.

For AI workloads such as Transformer Attention, FPGA hardware can significantly accelerate matrix operations.

---

## Zynq UltraScale+ MPSoC

The Zynq UltraScale+ MPSoC combines:

- ARM Cortex-A53 Processing System
- Programmable FPGA Logic
- Memory Controllers
- Peripheral Interfaces

This architecture enables hardware/software co-design.

---

## Processing System (PS)

The Processing System contains the ARM processors that execute embedded software.

Responsibilities include:

- Running drivers
- Sending data to FPGA
- Reading hardware results

---

## Programmable Logic (PL)

The Programmable Logic contains the FPGA fabric.

The custom Attention Accelerator will be implemented inside the PL.

---

## ZCU102 Board

The target hardware platform for this project.

Provides:

- Zynq UltraScale+ MPSoC
- DDR Memory
- Ethernet
- USB
- UART
- HDMI

---

## Vivado

Vivado is AMD's FPGA design software.

Used for:

- Hardware design
- RTL simulation
- IP integration
- Bitstream generation
- Hardware platform export

---

## Hardware Platform (.xsa)

The .xsa file describes the hardware configuration.

It is imported into Vitis so software development matches the hardware design.

---

# Work Completed

- Studied FPGA fundamentals.
- Learned Zynq UltraScale+ architecture.
- Understood PS and PL.
- Studied Vivado workflow.
- Created (or planned) the first Vivado Block Design.

---

# Challenges

- Understanding the difference between software execution and hardware implementation.
- Learning the FPGA design workflow.

---

# Outcome

Developed a conceptual understanding of the hardware platform that will host the Attention Accelerator.

Prepared for Block Design configuration and hardware/software integration.

---

# Next Steps

- Configure the Processing System inside Vivado.
- Export the hardware platform (.xsa).
- Begin Vitis platform creation.
