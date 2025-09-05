# RISC-V Campus Navigator

An embedded navigation system built on RISC-V architecture that finds optimal routes between University of Toronto campus libraries using real-time GPS integration and VGA display output.

## Features

- **Shortest Path Algorithm**: Implements Dijkstra's algorithm to compute optimal routes across 25+ campus intersection nodes
- **Real-Time GPS Integration**: Arduino-based GPS sensor automatically detects user location for dynamic starting point selection
- **Interactive VGA Display**: 320x240 pixel campus map visualization with dynamic path overlay
- **Memory-Mapped I/O Interface**: Direct hardware control through RISC-V processor peripheral interfaces
- **Multi-Input Control**: Support for manual navigation via switches/buttons and automatic GPS positioning

## System Architecture

### Hardware Components
- **RISC-V Processor**: Main processing unit with memory-mapped I/O capabilities
- **DE1-SoC FPGA Board**: Primary development platform
- **VGA Display**: 320x240 resolution output for map visualization
- **Arduino with GPS Module**: Real-time location detection via serial communication
- **Input Peripherals**: Switches and buttons for manual destination selection

### Software Components
- **Pathfinding Engine**: Dijkstra's algorithm implementation for route optimization
- **Graphics Renderer**: VGA frame buffer management (153.6KB bitmap array)
- **I/O Drivers**: Memory-mapped peripheral control and interrupt handlers
- **GPS Interface**: Serial communication protocol for Arduino integration

## Navigation System

The system supports navigation to four major campus libraries:
- Robarts Library
- Trinity College Library
- Gerstein Science Information Centre
- Sandford Fleming Library

### User Interaction Modes

1. **Manual Mode**: Use switches to select destination library and buttons for manual starting point selection
2. **GPS Mode**: Automatic starting point detection based on real-time GPS coordinates
3. **Hybrid Mode**: GPS starting point with manual destination selection

## Technical Implementation

### Memory-Mapped I/O
- Switch input polling for destination selection
- Button interrupt handlers for navigation control
- VGA display control for graphics output
- Serial communication interface for GPS data

### Graphics System
- Campus map stored as 320x240 bitmap array
- Real-time path rendering with color-coded visualization:
  - **Green**: Starting point
  - **Cyan**: Destination library
  - **Blue**: Optimal path route

### GPS Integration
- Serial communication protocol between Arduino and FPGA
- Coordinate conversion from GPS data to campus map coordinates
- Real-time position updates for dynamic navigation

## Getting Started

### Prerequisites
- DE1-SoC FPGA development board
- VGA-compatible display
- Arduino with GPS sensor module
- RISC-V toolchain for compilation

### Building and Running
1. Compile the RISC-V firmware using the provided toolchain
2. Program the FPGA with the system design
3. Connect VGA display and Arduino GPS module
4. Upload Arduino GPS firmware
5. Power on system and select navigation mode

## Usage

1. **System Startup**: Campus map displays on VGA monitor
2. **Destination Selection**: Use switches to choose target library
3. **Starting Point**: Either use GPS auto-detection or manual button selection
4. **Route Calculation**: System computes and displays optimal path in real-time
5. **Navigation**: Follow blue path overlay on campus map display

## Technical Specifications

- **Resolution**: 320x240 pixels
- **Memory Usage**: 153.6KB frame buffer
- **GPS Accuracy**: ±3 meter positioning
- **Path Computation**: Sub-100ms algorithm execution
- **Communication**: 9600 baud serial interface
- **Display Refresh**: 60Hz VGA output

## Project Structure

```
├── src/
│   ├── main.c              # Main system control
│   ├── dijkstra.c          # Pathfinding algorithm
│   ├── vga_driver.c        # VGA display control
│   ├── gpio_handler.c      # Switch/button input
│   └── gps_interface.c     # Serial communication
├── arduino/
│   └── gps_module.ino      # Arduino GPS firmware
├── assets/
│   └── campus_map.h        # Bitmap array data
└── docs/
    └── system_design.pdf   # Detailed architecture
```
