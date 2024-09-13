# Volative

 
![Progress API Rest](https://img.shields.io/badge/API_REST-25%25-orange) ![Progress Frontend](https://img.shields.io/badge/Webpage-0%25-red) ![Progress](https://img.shields.io/badge/Client-0%25-red)


Volative is a tool originally conceived to collaborate with the  [Voice Over](https://github.com/mrthinger/wow-voiceover)  project. It provides a system that allows collaborators from the project to offer their GPUs for voice generation.

## Project Overview
Volative serves as a bridge between GPU owners and the voice generation task. By distributing voice generation requests to contributors who provide their GPUs, it helps reduce the computing load, thus speeding up the voice synthesis process. The project integrates directly with the Voice Over project, enabling real-time, high-quality voice generation for its applications, such as in video game narration or character dialogue.


## Technologies
  
The backbone of the project is supported by various technologies and open-source projects. The main technologies used include:

<table>
  <tr>
    <td style="text-align:center;">
      <a href="https://coqui.ai/">
        <img src="https://img.shields.io/badge/Coqui_AI-black?style=for-the-badge&logo=data:image/svg+xml;base64,PD94bWwgdmVyc2lvbj0iMS4wIiBlbmNvZGluZz0iVVRGLTgiPz4KPCFET0NUWVBFIHN2ZyBQVUJMSUMgIi0vL1czQy8vRFREIFNWRyAxLjEvL0VOIiAiaHR0cDovL3d3dy53My5vcmcvR3JhcGhpY3MvU1ZHLzEuMS9EVEQvc3ZnMTEuZHRkIj4KPHN2ZyB4bWxucz0iaHR0cDovL3d3dy53My5vcmcvMjAwMC9zdmciIHZlcnNpb249IjEuMSIgd2lkdGg9IjEyN3B4IiBoZWlnaHQ9IjEyN3B4IiBzdHlsZT0ic2hhcGUtcmVuZGVyaW5nOmdlb21ldHJpY1ByZWNpc2lvbjsgdGV4dC1yZW5kZXJpbmc6Z2VvbWV0cmljUHJlY2lzaW9uOyBpbWFnZS1yZW5kZXJpbmc6b3B0aW1pemVRdWFsaXR5OyBmaWxsLXJ1bGU6ZXZlbm9kZDsgY2xpcC1ydWxlOmV2ZW5vZGQiIHhtbG5zOnhsaW5rPSJodHRwOi8vd3d3LnczLm9yZy8xOTk5L3hsaW5rIj4KPGc+PHBhdGggc3R5bGU9Im9wYWNpdHk6MC45ODgiIGZpbGw9IiM2N2IyOTYiIGQ9Ik0gMjAuNSwtMC41IEMgMjUuNSwtMC41IDMwLjUsLTAuNSAzNS41LC0wLjVDIDQzLjk5NjcsMi42NTg5NiA1MC4zMyw4LjMyNTYyIDU0LjUsMTYuNUMgNTcuMTQ1OSwxNy4xNjQ0IDU5Ljk3OTIsMTcuNDk3OCA2MywxNy41QyA2Ni4yNTE1LDE3LjQ4MDkgNjkuMDg0OSwxNi44MTQyIDcxLjUsMTUuNUMgNzUuMzE5OCw3LjY3ODM0IDgxLjMxOTgsMi4zNDUwMSA4OS41LC0wLjVDIDk0LjUsLTAuNSA5OS41LC0wLjUgMTA0LjUsLTAuNUMgMTE2LjU1Miw0LjIxNTY5IDEyMy44ODYsMTIuODgyNCAxMjYuNSwyNS41QyAxMjYuNSwyNy41IDEyNi41LDI5LjUgMTI2LjUsMzEuNUMgMTI1LjQzMSwzNy4xNDU5IDEyMy4wOTcsNDIuMzEyNSAxMTkuNSw0N0MgMTIyLjk1OSw1My41NDQ2IDEyNS4yOTIsNjAuMzc3OSAxMjYuNSw2Ny41QyAxMjYuNSw3MC4xNjY3IDEyNi41LDcyLjgzMzMgMTI2LjUsNzUuNUMgMTE5LjM2MiwxMDQuOTY0IDEwMC42OTUsMTIxLjk2NCA3MC41LDEyNi41QyA2NS4xNjY3LDEyNi41IDU5LjgzMzMsMTI2LjUgNTQuNSwxMjYuNUMgMjYuODEyOCwxMjIuODAzIDguNDc5NTEsMTA3LjgwMyAtMC41LDgxLjVDIC0wLjUsNzQuNSAtMC41LDY3LjUgLTAuNSw2MC41QyAxLjE4OTIyLDU1Ljk1OTMgMy4xODkyMiw1MS40NTkzIDUuNSw0N0MgMy4wNzk0OSw0My42NDkzIDEuMDc5NDksNDAuMTQ5MyAtMC41LDM2LjVDIC0wLjUsMzEuMTY2NyAtMC41LDI1LjgzMzMgLTAuNSwyMC41QyAzLjUsMTAuNSAxMC41LDMuNSAyMC41LC0wLjUgWiIvPjwvZz4KPGc+PHBhdGggc3R5bGU9Im9wYWNpdHk6MSIgZmlsbD0iI2Y4ZmJmYSIgZD0iTSAyMS41LDUuNSBDIDQyLjM0NDQsNC4xNzY3MiA1MS44NDQ0LDEzLjg0MzQgNTAsMzQuNUMgNDUuMTExNiw0Ny4wMzEgMzUuOTQ0OSw1Mi41MzEgMjIuNSw1MUMgNi41NjE1LDQ0LjE4NzYgMS43MjgxNywzMi42ODc2IDgsMTYuNUMgMTEuMzM1OCwxMS4yNjg1IDE1LjgzNTgsNy42MDE4NCAyMS41LDUuNSBaIi8+PC9nPgo8Zz48cGF0aCBzdHlsZT0ib3BhY2l0eToxIiBmaWxsPSIjZjhmYmZhIiBkPSJNIDkwLjUsNS41IEMgMTA5LjY2NywzLjg0Mzg0IDExOS41MDEsMTIuNTEwNSAxMjAsMzEuNUMgMTE2LjA2NSw0Ni4wNTU5IDEwNi41NjUsNTIuNTU1OSA5MS41LDUxQyA3NS41NjkxLDQ0LjIxNDkgNzAuNzM1NywzMi43MTQ5IDc3LDE2LjVDIDgwLjMzNTgsMTEuMjY4NSA4NC44MzU4LDcuNjAxODQgOTAuNSw1LjUgWiIvPjwvZz4KPGc+PHBhdGggc3R5bGU9Im9wYWNpdHk6MSIgZmlsbD0iIzYwYWY5MiIgZD0iTSAyNC41LDE0LjUgQyA0MC44NDI5LDEzLjAxMDcgNDguMzQyOSwyMC4zNDQgNDcsMzYuNUMgMzkuMDE3LDUwLjM1NDUgMjkuMDE3LDUyLjAyMTIgMTcsNDEuNUMgMTEuMDg2NSwzMC4wODIzIDEzLjU4NjUsMjEuMDgyMyAyNC41LDE0LjUgWiIvPjwvZz4KPGc+PHBhdGggc3R5bGU9Im9wYWNpdHk6MSIgZmlsbD0iIzYwYWY5MiIgZD0iTSA4Ny41LDE0LjUgQyAxMDUuMTE4LDEyLjYxNSAxMTIuNjE4LDIwLjI4MTcgMTEwLDM3LjVDIDEwMy4wODUsNDkuMTM3NyA5My45MTc5LDUxLjMwNDQgODIuNSw0NEMgNzQuNDE0MiwzMi4zNDc2IDc2LjA4MDgsMjIuNTE0MiA4Ny41LDE0LjUgWiIvPjwvZz4KPGc+PHBhdGggc3R5bGU9Im9wYWNpdHk6MC41NjkiIGZpbGw9IiM4Y2M1YjAiIGQ9Ik0gNzEuNSwxNS41IEMgNjkuMDg0OSwxNi44MTQyIDY2LjI1MTUsMTcuNDgwOSA2MywxNy41QyA1OS45NzkyLDE3LjQ5NzggNTcuMTQ1OSwxNy4xNjQ0IDU0LjUsMTYuNUMgNjAuMjU4NiwxNi43ODU3IDY1LjkyNTIsMTYuNDUyNCA3MS41LDE1LjUgWiIvPjwvZz4KPGc+PHBhdGggc3R5bGU9Im9wYWNpdHk6MSIgZmlsbD0iI2ZkZmVmZCIgZD0iTSA1Ni41LDIyLjUgQyA2MC41LDIyLjUgNjQuNSwyMi41IDY4LjUsMjIuNUMgNjcuMjUxNiw0Mi40MDY0IDc2LjQxODMsNTMuNzM5NyA5Niw1Ni41QyAxMDIuNjk3LDU2Ljc4NDEgMTA4Ljg2NCw1NS4xMTc0IDExNC41LDUxLjVDIDExOS4wNiw1OC44NzEgMTIwLjU2LDY2Ljg3MSAxMTksNzUuNUMgMTE0LjE4LDgyLjMwMzIgMTA3LjY4LDg2LjgwMzIgOTkuNSw4OUMgNzMuNzAyNiw5Ni42MTEgNDguMDM1OSw5Ni4yNzc3IDIyLjUsODhDIDQuMjU1MzQsODAuNzcyOCAwLjI1NTM0Miw2OC42MDYyIDEwLjUsNTEuNUMgMjYuMjAyNSw2MC4wMDA4IDQwLjAzNTksNTcuNjY3NSA1Miw0NC41QyA1Ni4wMDA0LDM3LjcxMDggNTcuNTAwNCwzMC4zNzc0IDU2LjUsMjIuNSBaIi8+PC9nPgo8Zz48cGF0aCBzdHlsZT0ib3BhY2l0eToxIiBmaWxsPSIjNjRiMTk1IiBkPSJNIDQ1LjUsNzIuNSBDIDUwLjk4NjgsNzEuOTYxNSA1My4xNTM0LDc0LjI5NDkgNTIsNzkuNUMgNDkuNzYyNyw4My4wMTk5IDQ3LjA5NjEsODMuMzUzMiA0NCw4MC41QyA0My4xMDkzLDc3LjUwMjQgNDMuNjA5Myw3NC44MzU3IDQ1LjUsNzIuNSBaIi8+PC9nPgo8Zz48cGF0aCBzdHlsZT0ib3BhY2l0eToxIiBmaWxsPSIjNjZiMjk2IiBkPSJNIDc0LjUsNzIuNSBDIDgwLjk4ODksNzIuMTU2MyA4Mi45ODg5LDc0Ljk4OTYgODAuNSw4MUMgNzQuMTQ3NSw4My4zOTg5IDcxLjY0NzUsODEuMjMyMyA3Myw3NC41QyA3My43MTcyLDczLjk1NTggNzQuMjE3Miw3My4yODkxIDc0LjUsNzIuNSBaIi8+PC9nPgo8Zz48cGF0aCBzdHlsZT0ib3BhY2l0eToxIiBmaWxsPSIjZmNmZGZkIiBkPSJNIDcuNSw4Ny41IEMgMzkuNzI2MSwxMDMuMDQxIDczLjA1OTQsMTA0LjU0MSAxMDcuNSw5MkMgMTEwLjcwMSw4OS43MzI3IDExNC4wMzQsODguMDY2IDExNy41LDg3QyAxMDUuNzM1LDEwOC45NzkgODcuMjM1MywxMjAuMTQ2IDYyLDEyMC41QyAzNy4zNDk1LDExOS43NzYgMTkuMTgyOCwxMDguNzc2IDcuNSw4Ny41IFoiLz48L2c+Cjwvc3ZnPgo=">
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