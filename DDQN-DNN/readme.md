# DNN-based Traffic Light Control System

This repository contains the implementation of a Deep Neural Network (DNN) based traffic light control system using Double Deep Q-Networks (DDQN).

## Table of Contents

1. [Introduction](#introduction)
2. [Method](#method)
3. [Experiments](#experiments)
4. [Conclusions](#conclusions)

---

### 1. Introduction

In this project, we explore the application of Deep Reinforcement Learning (DRL) for traffic light control in urban intersections. The goal is to optimize traffic flow and reduce waiting times using DDQN.

### 2. Method

The method involves training a DDQN to learn the optimal policy for traffic light control. The state space includes the current queue lengths and waiting times at each intersection. The action space consists of different traffic light settings.

#### Formulas

The Q-value update rule in DDQN is given by:
\[ Q(s, a) \leftarrow Q(s, a) + \alpha \left[ r + \gamma \max_{a'} Q\left(s', a'\right) - Q(s, a) \right] \]
where:
- \( Q(s, a) \) is the Q-value for state \( s \) and action \( a \)
- \( \alpha \) is the learning rate
- \( r \) is the reward received after taking action \( a \) in state \( s \)
- \( \gamma \) is the discount factor
- \( s' \) is the next state

### 3. Experiments

We conducted experiments using a simulated environment with multiple intersections. The performance of the DDQN controller was compared against traditional fixed-time controllers.

#### Results

The results showed significant improvements in traffic flow efficiency and reduced average waiting times.

#### 4. Conclusions

This project demonstrates the potential of using DDQN for adaptive traffic light control. Future work will focus on scaling the approach to real-world scenarios and integrating with existing traffic management systems.

The experiments were conducted using the traffic simulation platform **SUMO**, testing signal control for multiple intersections. Different traffic flows and signal cycle configurations were used to validate the adaptability and superiority of the **DuelingDDQN-DNN** algorithm in various scenarios.

