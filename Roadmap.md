### 📦 Phase 1: Foundation & Environment Validation (Days 1–6)
*Target: Master the underlying mathematical equations and establish the bare-metal software boot loop.*
* **Days 1–2: Attention Math Crash Course:** Implement a reference algorithm for Scaled Dot-Product Attention in standard Python/C to study data flow and quantization effects.
* **Days 3–4: Zynq UltraScale+ Layout:** Open Vivado 2025.2, configure the Zynq UltraScale+ Processing System block targeting the ZCU102, and export the pre-synthesis `.xsa` platform profile.
* **Days 5–6: Renode Virtual Boot:** Initialize the Vitis 2025.2 environment, generate a simple "Hello World" standalone component, and successfully boot the `.elf` binary via Renode's built-in `zynqmp.repl` console.

### ⚙️ Phase 2: RTL Hardware Design & Simulation (Days 7–13)
*Target: Program the accelerator engine in Verilog and verify logic via behavioral waveforms.*
* **Days 7–8: Core Datapath Architecture:** Design a parameterized hardware module using parallel Multiply-Accumulate (MAC) paths designed to infer internal FPGA DSP units.
* **Days 9–10: AXI-Lite Register Mapping:** Wrap the datapath inside an AXI-Lite bus wrapper mapping the IP directly onto the processor's data highway:
    * `0x40000000`: Vector Q Input Register
    * `0x40000004`: Vector K Input Register
    * `0x40000008`: Control & Status Register (Start / Done handshakes)
    * `0x4000000C`: Accumulator Output Register
* **Days 11–13: Logic Verification (Vivado XSIM):** Author a structured HDL testbench, inject mock weight matrices, and verify cycle-accurate execution using Vivado's native waveform viewer.

### 🔌 Phase 3: Software Drivers & Behavioral Emulation (Days 14–19)
*Target: Create the virtual peripheral layer in Renode and write bare-metal hardware drivers.*
* **Days 14–15: Renode Peripheral Modeling:** Code a lightweight Python script inside Renode to capture CPU transactional writes at `0x40000000`, behaviorally compute the dot product, and drive status flags.
* **Days 16–17: Driver Development:** Implement low-level C macros (`Xil_Out32` / `Xil_In32`) inside Vitis to abstract register configuration, clock cycles, and data transfers.
* **Days 18–19: Embedded Softmax Implementation:** Develop the exponential and division layers of the transformer layer in optimized C to run natively on the ARM CPU core.

### 📊 Phase 4: Integration, Benchmarking & Wrap-up (Days 20–25)
*Target: Execute the unified system inside the emulator, perform benchmarking, and package the repository.*
* **Days 20–22: Co-Simulation Run:** Flash the unified binary file to Renode, pass entire token arrays through the driver pipeline, and capture attention output arrays over the virtual UART link.
* **Days 23–24: Performance Benchmarking:** Measure and log execution timing differences between pure software processing and hardware-accelerated processing loops.
* **Day 25 (July 25th): Repository Freeze:** Polish source comments, organize code directories, and finalize documentation.

---

## 🛠️ Toolchain Setup
To run and develop this project locally, make sure your machine has the following software stacks installed:
1. **AMD Vivado Design Suite (2025.2):** Used for RTL hardware description, packaging IP, and logic simulation.
2. **AMD Vitis Unified IDE (2025.2):** Used for platform compilation, Driver layer code generation, and C application development.
3. **Antmicro Renode Emulator:** Functional, instruction-level multi-node system emulator used to execute software on virtual boards without physical hardware constraints.

---

## 💡 Daily Engineering Protocol
Since we operate on an optimized timeline of **1 - 1.5 hours per day**, team members must maintain strict engineering hygiene:
* **Atomicity:** Work on exactly one item from the roadmap per day. Do not jump ahead until the current day's verification checks pass.
* **State Continuity:** If an error block or compilation failure stalls work at the end of a session, document the exact terminal dump and pointer trace inside a scratch file so the next session can resume immediately without retracing steps.
"""

with open("README.md", "w", encoding="utf-8") as f:
    f.write(markdown_content)

print("Generated README.md successfully.")