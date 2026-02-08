// Convex schema for CalmMateAI users
// Run: npx convex dev (from project root) to push this schema

import { defineSchema, defineTable } from "convex/server";
import { v } from "convex/values";

export default defineSchema({
  users: defineTable({
    email: v.string(),
    name: v.string(),
    password: v.string(), // stored hashed (from Python)
  }).index("by_email", ["email"]),
});
