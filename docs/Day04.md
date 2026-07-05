# Day 04 - FPGA Development Environment Setup and Zynq Architecture

**Date:** 05 July 2026

---

# Objective

Understand the FPGA development workflow, learn the architecture of the Zynq UltraScale+ MPSoC, and prepare the software tools required for hardware development.

---

# Topics Studied

- FPGA Fundamentals
- CPU vs FPGA
- Zynq UltraScale+ MPSoC
- Processing System (PS)
- Programmable Logic (PL)
- Vivado Design Suite
- Vitis Unified IDE
- Renode Emulator
- Block Design
- Hardware Platform (.xsa)

---

# Concepts Learned

## FPGA

An FPGA (Field Programmable Gate Array) is a programmable hardware device that allows custom digital circuits to be implemented after manufacturing.

Unlike CPUs, FPGAs execute hardware logic directly and can perform many operations in parallel.

---

## CPU vs FPGA

CPU

- Executes software instructions.
- Optimized for sequential processing.
- Flexible for many applications.

FPGA

- Implements custom digital circuits.
- Optimized for parallel computation.
- Ideal for accelerating AI workloads.

---

## Zynq UltraScale+ MPSoC

The Zynq UltraScale+ combines:

- ARM Cortex-A53 Processing System
- Programmable FPGA Logic
- Memory Controllers
- Peripheral Interfaces

This enables hardware and software to work together on the same chip.

---

## Processing System (PS)

The Processing System contains the ARM processors responsible for:

- Running embedded software
- Executing drivers
- Sending data to FPGA
- Reading computation results

---

## Programmable Logic (PL)

The Programmable Logic is the FPGA fabric where the custom Attention Accelerator will be implemented.

---

## Vivado

Vivado is AMD's FPGA design environment.

Responsibilities include:

- Creating hardware designs
- Connecting IP blocks
- Running simulations
- Exporting the hardware platform

---

## Vitis

Vitis is used to develop embedded software for the ARM processor.

Applications written in Vitis communicate with the FPGA hardware.

---

## Renode

Renode is a virtual hardware emulator that allows software development and testing without requiring a physical FPGA board.

---

## Hardware Platform (.xsa)

The .xsa file represents the exported hardware configuration from Vivado.

It is imported into Vitis to ensure the software matches the hardware design.

---

# Work Completed

- Studied the FPGA development workflow.
- Learned the Zynq UltraScale+ architecture.
- Understood the role of the Processing System and Programmable Logic.
- Learned the purpose of Vivado, Vitis, and Renode.
- Planned the installation of the FPGA development environment.

---

# Challenges

- Understanding the complete FPGA toolchain.
- Distinguishing the responsibilities of Vivado, Vitis, and Renode.

---

# Outcome

Developed a clear understanding of the complete hardware/software development workflow required for the Attention Accelerator project.

Prepared to install the FPGA development environment and begin hardware platform creation.

---

# Next Steps

- Install Vivado and Vitis.
- Create the first Vivado project.
- Configure the Zynq UltraScale+ Processing System.
- Generate the hardware platform (.xsa).
