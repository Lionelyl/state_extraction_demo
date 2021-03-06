import { TimeAxisLabelFormatterOption } from './../coord/axisCommonTypes.js';
import { TimeScaleTick } from './types.js';
import { LocaleOption } from '../core/locale.js';
import Model from '../model/Model.js';
export declare const ONE_SECOND = 1000;
export declare const ONE_MINUTE: number;
export declare const ONE_HOUR: number;
export declare const ONE_DAY: number;
export declare const ONE_YEAR: number;
export declare const defaultLeveledFormatter: {
    year: string;
    month: string;
    day: string;
    hour: string;
    minute: string;
    second: string;
    millisecond: string;
    none: string;
};
export declare const fullLeveledFormatter: {
    year: string;
    month: string;
    day: string;
    hour: string;
    minute: string;
    second: string;
    millisecond: string;
};
export declare type PrimaryTimeUnit = 'millisecond' | 'second' | 'minute' | 'hour' | 'day' | 'month' | 'year';
export declare type TimeUnit = PrimaryTimeUnit | 'half-year' | 'quarter' | 'week' | 'half-week' | 'half-day' | 'quarter-day';
export declare const primaryTimeUnits: PrimaryTimeUnit[];
export declare const timeUnits: TimeUnit[];
export declare function pad(str: string | number, len: number): string;
export declare function getPrimaryTimeUnit(timeUnit: TimeUnit): PrimaryTimeUnit;
export declare function isPrimaryTimeUnit(timeUnit: TimeUnit): boolean;
export declare function getDefaultFormatPrecisionOfInterval(timeUnit: PrimaryTimeUnit): PrimaryTimeUnit;
export declare function format(time: unknown, template: string, isUTC: boolean, lang?: string | Model<LocaleOption>): string;
export declare function leveledFormat(tick: TimeScaleTick, idx: number, formatter: TimeAxisLabelFormatterOption, lang: string | Model<LocaleOption>, isUTC: boolean): string;
export declare function getUnitFromValue(value: number | string | Date, isUTC: boolean): PrimaryTimeUnit;
export declare function getUnitValue(value: number | Date, unit: TimeUnit, isUTC: boolean): number;
export declare function fullYearGetterName(isUTC: boolean): "getUTCFullYear" | "getFullYear";
export declare function monthGetterName(isUTC: boolean): "getUTCMonth" | "getMonth";
export declare function dateGetterName(isUTC: boolean): "getUTCDate" | "getDate";
export declare function hoursGetterName(isUTC: boolean): "getUTCHours" | "getHours";
export declare function minutesGetterName(isUTC: boolean): "getUTCMinutes" | "getMinutes";
export declare function secondsGetterName(isUTC: boolean): "getUTCSeconds" | "getSeconds";
export declare function millisecondsGetterName(isUTC: boolean): "getUTCMilliseconds" | "getMilliseconds";
export declare function fullYearSetterName(isUTC: boolean): "setUTCFullYear" | "setFullYear";
export declare function monthSetterName(isUTC: boolean): "setUTCMonth" | "setMonth";
export declare function dateSetterName(isUTC: boolean): "setUTCDate" | "setDate";
export declare function hoursSetterName(isUTC: boolean): "setUTCHours" | "setHours";
export declare function minutesSetterName(isUTC: boolean): "setUTCMinutes" | "setMinutes";
export declare function secondsSetterName(isUTC: boolean): "setUTCSeconds" | "setSeconds";
export declare function millisecondsSetterName(isUTC: boolean): "setUTCMilliseconds" | "setMilliseconds";
