// 1. Basic Types
let name: string = "Alice";
let age: number = 30;
let isActive: boolean = true;

// Array & Tuple
let numbers: number[] = [1, 2, 3];
let coordinates: [number, number] = [40.7128, -74.0060];

// Enum
enum Color { Red, Green, Blue }
let color: Color = Color.Green;

// Any
let variable: any = "Could be anything";

// Void - used in functions that don’t return a value
function logMessage(message: string): void {
    console.log(message);
}

// Null & Undefined
let u: undefined = undefined;
let n: null = null;

// Never - represents values that never occur
function error(message: string): never {
    throw new Error(message);
}

// 2. Type Assertions (Type Casting)
let someValue: any = "This is a string";
let strLength: number = (someValue as string).length;

// 3. Functions
function add(x: number, y: number): number {
    return x + y;
}

// Optional and Default Parameters
function greet(name: string, greeting: string = "Hello"): string {
    return `${greeting}, ${name}`;
}

// Arrow Functions
const square = (n: number): number => n * n;

// 4. Objects & Interfaces

// Object Type
let user: { name: string; age: number } = { name: "Alice", age: 25 };

// Interface
interface User {
    name: string;
    age: number;
}
const userObj: User = { name: "Alice", age: 25 };

// Optional Properties
interface OptionalUser {
    name: string;
    age?: number;  // Optional property
}

// Readonly Properties
interface ReadonlyUser {
    readonly id: number;
    name: string;
}

// 5. Classes

// Basic Class
class Person {
    name: string;
    
    constructor(name: string) {
        this.name = name;
    }

    greet(): string {
        return `Hello, ${this.name}`;
    }
}

// Access Modifiers
class Car {
    public model: string;
    private year: number;
    protected color: string;

    constructor(model: string, year: number, color: string) {
        this.model = model;
        this.year = year;
        this.color = color;
    }
}

// Inheritance
class Animal {
    move() {
        console.log("Moving along!");
    }
}

class Dog extends Animal {
    bark() {
        console.log("Woof!");
    }
}

// 6. Generics

// Generic Functions
function identity<T>(value: T): T {
    return value;
}
let output = identity<string>("Hello");

// Generic Classes
class Box<T> {
    contents: T;
    constructor(contents: T) {
        this.contents = contents;
    }
}

// 7. Union & Intersection Types

// Union Types
let id: number | string;
id = 101;
id = "ABC";

// Intersection Types
interface Drivable {
    drive(): void;
}
interface Flyable {
    fly(): void;
}
type Vehicle = Drivable & Flyable;

// 8. Type Aliases

type StringOrNumber = string | number;
let data: StringOrNumber = "Hello";

// 9. Utility Types

// Partial, Required, and Readonly
interface UtilityUser {
    name: string;
    age?: number;
}
let partialUser: Partial<UtilityUser>;      // All properties optional
let requiredUser: Required<UtilityUser>;    // All properties required
let readonlyUser: Readonly<UtilityUser>;    // All properties readonly

// Pick & Omit
type PickUser = Pick<UtilityUser, "name">;
type OmitUser = Omit<UtilityUser, "age">;

// 10. Modules

// Export and Import
// user.ts
export interface ExportedUser { name: string; age: number; }

// main.ts
import { ExportedUser } from './user';

// 11. Type Guards

function isString(value: any): value is string {
    return typeof value === "string";
}

// 12. Type Casting (Type Assertions)

let someUnknown: unknown = "Hello";
let length: number = (someUnknown as string).length;

// 13. Conditional Types

type Message<T> = T extends string ? string : number;
let msg1: Message<string>;  // string
let msg2: Message<number>;  // number

// 14. Optional Chaining and Nullish Coalescing

// Optional Chaining (?.)
let userOrNull: UtilityUser | null = null;
console.log(userOrNull?.name);  // Won't throw an error if null

// Nullish Coalescing (??)
let nameOrDefault = userOrNull?.name ?? "Anonymous";

// 15. Non-null Assertion

function getValue(input?: string) {
    return input!.length;  // Asserts input is non-nullable
}
