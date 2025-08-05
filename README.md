
<img width="1536" height="1024" alt="ChatGPT Image 5 ago 2025, 03_27_22 p m" src="https://github.com/user-attachments/assets/9a6dda14-a76c-4dbc-b4b3-6dabffa53b23" />

**DAMvulnerable** es una colección de laboratorios prácticos diseñados para explorar vulnerabilidades reales en esquemas criptográficos post-cuánticos. Su objetivo es ofrecer un entorno controlado para que investigadores, estudiantes y entusiastas de la seguridad puedan aprender, practicar y comprender fallos que pueden presentarse en implementaciones del mundo real.

## Objetivo

Proporcionar un conjunto de retos de seguridad y criptografía avanzada que permitan desarrollar habilidades prácticas en:

- Criptoanálisis post-cuántico
- Explotación de fallos de implementación
- Técnicas avanzadas de auditoría y testing
- Modelos de ataque teóricos llevados a la práctica

## Lista de retos

1. **Broken Parameter Selection - Kyber**  
2. **MinRank Madness - Rainbow**  
3. **Key Confusion - Dilithium**  
4. **Message Leakage - NTRU**  
5. **Hashing Trapdoor - SPHINCS+**  
6. **Fake Public Key Injection - Kyber**  
7. **Timing Side-Channel - Saber**  
8. **Broken KEM Interface - KEM genérico**  
9. **Weak Randomness in Signature - Falcon**  
10. **Legacy-Fallback Downgrade - Hybrid (PQC + RSA)**

## Reducción de dificultad

En su concepción inicial, la dificultad de los laboratorios era **muy elevada**, con parámetros y escenarios que requerían un alto nivel de conocimiento matemático, experiencia en criptoanálisis y recursos computacionales significativos.  

Con el fin de hacer el contenido más accesible y favorecer un aprendizaje progresivo, la dificultad fue **reducida considerablemente**:
- Parámetros ajustados para que los ataques sean reproducibles en equipos personales.
- Escenarios simplificados sin perder la lógica y esencia del fallo.
- Código más legible y documentado para facilitar la comprensión.

## Requisitos

- Python 3.9+  
- Herramientas criptográficas específicas según el laboratorio    

## Uso

Cada laboratorio incluye su propio README con instrucciones específicas, comandos de ejecución y soluciones esperadas. Se recomienda seguir el orden propuesto para ir incrementando el nivel de dificultad.

## 📜 Créditos

Desarrollado por [**HackSyndicate**](https://www.hacksyndicate.xyz)  
Coordinado por [**Mauro Carrillo (Pr00f)**](https://www.linkedin.com/in/mauro-carrillo-7a326a208)
