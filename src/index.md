---
title: Hardware & Assembly 
author: "Prof. Calvin"
subtitle: "CS 371"
format: html
---

# Calendar

<!-- https://www.cs.unc.edu/~kakiryan/teaching/311-sp26/311-sp26.html -->

|Week Num.|Week Date|Day One|Day Two|HW or Lab|
|:--:|:---|:----|:-------|:-------|
|0x0|01/11|[podman](00_podman.qmd)|[alpine](01_alpine.qmd)|[Enigma](02_enigma.qmd)|
|0x1|01/18|King Day|[printb](11_printb.qmd)|[macros](12_macros.qmd)|
|0x2|01/25|[SHA256](20_sha256.qmd)|[Endian](21_endian.qmd)|[SHAinC](22_shainc.qmd)|
|0x3|09/15|INTCEC|[Finite](30_finite.qmd)||
|0x4|09/22|[BigAdd](31_bigadd.qmd)|[Fermat](40_fermat.qmd)|[4096_t](32_4096_t.qmd)|
|0x5|09/29|IASC26|[KeyGen](41_keygen.qmd)|[RSAinC](42_rsainc.qmd)|
|0x6|10/06|[Euclid](50_euclid.qmd)|[ops_ui](51_ops_ui.qmd)|[BigRSA](52_bigrsa.qmd)|
|0x7|10/13|Middle|Assess||
|0x8|10/20|[Mounts](60_mounts.qmd)|[action](61_action.qmd)||
|0x9|10/27|[Stream](70_stream.qmd)|[malloc](71_malloc.qmd)|[list_t](72_list_t.qmd)|
|0bX|11/03|`break;`|[struct](80_struct.qmd)||
|0xA|11/10|[bchain](81_bchain.qmd)||               |
|0xB|11/17|[graphs](90_graphs.qmd)|[Merkle](91_merkle.qmd)|[heap_t](92_heap_t.qmd)|
|0xC|11/24|[Logics](A0_logics.qmd)|`break;`|
|0xD|12/01|||[BTCinC](A2_btcinc.qmd)|

*The final is described as [BTCinC](A2_btcinc.qmd) and is due [Tuesday, December 8th at 5:00 p.m.](https://my.willamette.edu/site/registrar/info/mywu-summative-evaluations).

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
- With great appreciation to a former fellow group member, [Kaki Ryan](https://www.cs.unc.edu/~kakiryan/), who is as smart as I wish I was and develops great course materials.

Course Description:

> A semester-long study of computer architecture and organization, information management, networking and communication, operating systems, or parallel and distributed computing that applies or extends the content of CS 271 or more advanced classes.

Semester Description:

>  This course provides a foundational understanding of how computers work at the hardware level, from binary data to instruction execution. Students will begin with binary arithmetic and Boolean algebra, developing the skills to reason about digital logic and data representation. The course then introduces the RISC-V assembly language, allowing students to explore how high-level instructions are translated into machine-level operations.

> Building on this knowledge, students will learn how a processor executes instructions by designing a single-cycle RISC-V datapath. Students will design and implement core processor components—including the Arithmetic Logic Unit (ALU) and the control unit—and integrate them into a working datapath. Using a graphical digital logic simulator, they will construct and test their designs by simulating real RISC-V instructions. By the end of the course, students will have a working understanding of the key architectural components of a processor and the logical structures that support them.

### [Prof. Calvin](mailto:ckdeutschbein@willamette.edu)

### Syllabus

- [Syllabus link](syllabus/syllabus.pdf)
