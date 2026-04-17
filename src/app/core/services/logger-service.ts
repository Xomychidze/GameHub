// services/logger.service.ts
import { Injectable } from '@angular/core';

export enum LogLevel {
  DEBUG = 0,
  INFO  = 1,
  WARN  = 2,
  ERROR = 3,
}

@Injectable({ providedIn: 'root' })
export class LoggerService {
  private level: LogLevel = LogLevel.DEBUG;

  debug(message: string, ...args: any[]) {
    this.log(LogLevel.DEBUG, '🐛 DEBUG', message, args);
  }

  info(message: string, ...args: any[]) {
    this.log(LogLevel.INFO, '📘 INFO', message, args);
  }

  warn(message: string, ...args: any[]) {
    this.log(LogLevel.WARN, '⚠️ WARN', message, args);
  }

  error(message: string, ...args: any[]) {
    this.log(LogLevel.ERROR, '🔴 ERROR', message, args);
  }

  private log(level: LogLevel, prefix: string, message: string, args: any[]) {
    if (level < this.level) return;

    const timestamp = new Date().toISOString();
    const output = `[${timestamp}] ${prefix}: ${message}`;

    if (level === LogLevel.ERROR) console.error(output, ...args);
    else if (level === LogLevel.WARN)  console.warn(output, ...args);
    else console.log(output, ...args);
  }
}
