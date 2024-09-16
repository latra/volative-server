# Volative

 
[![Progress API Rest](https://img.shields.io/badge/API_REST-25%25-orange)](https://github.com/latra/volative-server) [![Progress Frontend](https://img.shields.io/badge/Webpage-0%25-red)](https://github.com/latra/volative-webpage) [![Progress](https://img.shields.io/badge/Client-0%25-red)]()

Volative is a tool originally conceived to collaborate with the  [Voice Over](https://github.com/mrthinger/wow-voiceover)  project. It provides a system that allows collaborators from the project to offer their GPUs for voice generation.

## Project Overview
Volative serves as a bridge between GPU owners and the voice generation task. By distributing voice generation requests to contributors who provide their GPUs, it helps reduce the computing load, thus speeding up the voice synthesis process. The project integrates directly with the Voice Over project, enabling real-time, high-quality voice generation for its applications, such as in video game narration or character dialogue.

This project is divided in three main modules:
- Rest API
- Frontend Webpage
- Client Tool

## Technologies
  
The backbone of the project is supported by various technologies and open-source projects. The main technologies used include:

<table>
  <tr>
    <td style="text-align:center;">
      <a href="https://coqui.ai/">
        <img src="https://img.shields.io/badge/Coqui_AI-black?style=for-the-badge&logo=huggingface">
      </a>
    </td>
    <td style="text-align:center;">
      Used for text-to-speech (TTS) and voice cloning.
    </td>
  </tr>
  <tr>
    <td style="text-align:center;">
      <a href="https://fastapi.tiangolo.com/">
        <img src="https://img.shields.io/badge/Fast%20API-grey?style=for-the-badge&logo=fastapi">
      </a>
    </td>
    <td style="text-align:center;">
      A modern, fast (high-performance) web framework for building REST APIs with Python.
    </td>
  </tr>
  <tr>
    <td style="text-align:center;">
      <a href="https://es.react.dev/">
        <img src="https://img.shields.io/badge/REACT-black?style=for-the-badge&logo=react">
      </a>
    </td>
    <td style="text-align:center;">
      A JavaScript library used for building user interfaces, particularly for the frontend of the project.
    </td>
  </tr>
  <tr>
    <td style="text-align:center;">
      <a href="https://www.rabbitmq.com/">
        <img src="https://img.shields.io/badge/RabbitMQ-grey?style=for-the-badge&logo=rabbitmq">
      </a>
    </td>
    <td style="text-align:center;">
      A message-broker that facilitates communication between services, ensuring that voice generation requests are properly handled.
    </td>
  </tr>
  <tr>
    <td style="text-align:center;">
      <a href="https://www.postgresql.org/">
        <img src="https://img.shields.io/badge/Postgre_SQL-black?style=for-the-badge&logo=postgresql">
      </a>
    </td>
    <td style="text-align:center;">
      A robust, relational database used to manage the project’s data and request handling.
    </td>
  </tr>
</table>

## Acknowledgements
- [Voice Over](https://github.com/mrthinger/wow-voiceover/) - The main project that inspired and provided context for Volative's development.

## Authors
- [Paula "Latra" Gallucci](https://github.com/latra)