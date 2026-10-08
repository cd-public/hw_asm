---
title: Hardware & Assembly 
author: "Prof. Calvin"
subtitle: "CS 371"
format: html
---

# Calendar

<!-- https://www.cs.unc.edu/~kakiryan/teaching/311-sp26/311-sp26.html -->

|Week Num.|Week Date|T|R|Lab|
|:--:|:---|:----|:-------|:-------|
|0x0|01/11|Intro|Instructions| <!-- sure would like a compile to riscv asm, edit, simulate lab here -->
|0x1|01/18|Circuits|Transistors|
|0x2|01/25|Gates|Multiplex|Lab 1| <!-- out with multiplex, due after ~9 days -->
|0x3|02/01|Minimze|Karnaugh|
|0x4|02/08|Encoders|Adders|Lab 2| <!-- out with encoders, due after ALU  -->
|0x5|02/15|ALU|Registers|
|0x6|02/22|Timing|Performance|
|0x7|03/01|Pipelines|`lw`|Lab 3| <!-- out before pipeline, due after `lw`  -->
|0x8|03/08|RISC-V|Stages|Lab 4| <!-- out with R5, due between stack and hazard  -->
|0x9|03/15|Proc.|Stack|
|0bX|03/22|Hazard|Bypass|Lab 5| <!-- out with Hazard, due Security  -->
|0xA|03/29|Hierarchy|Cache|
|0xB|04/05|[`nop`](https://events.willamette.edu/e/7428)|Security|
|0xC|04/12|Spectre|Astarte|
|0xD|04/19|Isadora|`vcd2df`|

# Recordings

This isn't real, its a placeholder from a previous term.

<iframe width="560" height="315" src="https://www.youtube.com/embed/videoseries?si=aonYOyE6DyUx5Bfs&amp;list=PLRUtrB1tmoTs" title="YouTube video player" frameborder="0" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture; web-share" referrerpolicy="strict-origin-when-cross-origin" allowfullscreen></iframe>

# CS 371 "Hardware & Assembly" 

- Called:
    - CS 371: Advanced Systems Computing 
    - CS 371: Hardware Designs and Assembly Language
    - CS 371: Hardware and Assembly 
- The second semester class in a:
    - Compiled language, with
    - No garbage collector.
- In the second semester, one of the great $n$ systems
    - Operating System (OS)
    - Compiler
        - We cover the special case of compiler design from the level of hardware design.
    - Server.
- Taught this year in language-agnostic digital logic.
    - Though I expect you'll want to know C; Rust may be okay. 

Course Description:

> A semester-long study of computer architecture and organization, information management, networking and communication, operating systems, or parallel and distributed computing that applies or extends the content of CS 271 or more advanced classes.

Semester Description:

>  This course provides a foundational understanding of how computers work at the hardware level, from binary data to instruction execution. Students will begin with binary arithmetic and Boolean algebra, developing the skills to reason about digital logic and data representation. The course then introduces the RISC-V assembly language, allowing students to explore how high-level instructions are translated into machine-level operations.

> Building on this knowledge, students will learn how a processor executes instructions by designing a single-cycle RISC-V datapath. Students will design and implement core processor components—including the Arithmetic Logic Unit (ALU) and the control unit—and integrate them into a working datapath. Using a graphical digital logic simulator, they will construct and test their designs by simulating real RISC-V instructions. By the end of the course, students will have a working understanding of the key architectural components of a processor and the logical structures that support them.

### [Prof. Calvin](mailto:ckdeutschbein@willamette.edu)

### Syllabus

- [Syllabus link](syllabus/syllabus.pdf)

### Citation

- This course adapted from a course by [Kaki Ryan](https://www.cs.unc.edu/~kakiryan/teaching/311-sp26/311-sp26.html)
