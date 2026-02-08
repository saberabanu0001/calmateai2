// Convex user queries and mutations for CalmMateAI
// Called from Python via ConvexClient.query("users:getByEmail") etc.

import { query, mutation } from "./_generated/server";
import { v } from "convex/values";

/** Get one user by email (returns null if not found) */
export const getByEmail = query({
  args: { email: v.string() },
  handler: async (ctx, { email }) => {
    const user = await ctx.db
      .query("users")
      .withIndex("by_email", (q) => q.eq("email", email))
      .unique();
    return user;
  },
});

/** List all users (for compatibility with get_registered_users) */
export const list = query({
  args: {},
  handler: async (ctx) => {
    return await ctx.db.query("users").collect();
  },
});

/** Create a new user. Password must already be hashed in Python. */
export const create = mutation({
  args: {
    email: v.string(),
    name: v.string(),
    password: v.string(),
  },
  handler: async (ctx, { email, name, password }) => {
    const existing = await ctx.db
      .query("users")
      .withIndex("by_email", (q) => q.eq("email", email))
      .unique();
    if (existing) throw new Error("Email already registered");
    return await ctx.db.insert("users", { email, name, password });
  },
});

/** Update name and/or password for an existing user (password already hashed in Python) */
export const update = mutation({
  args: {
    email: v.string(),
    newName: v.string(),
    newPassword: v.optional(v.string()),
  },
  handler: async (ctx, { email, newName, newPassword }) => {
    const user = await ctx.db
      .query("users")
      .withIndex("by_email", (q) => q.eq("email", email))
      .unique();
    if (!user) return null;
    const patch = { name: newName };
    if (newPassword !== undefined) patch.password = newPassword;
    await ctx.db.patch(user._id, patch);
    return user._id;
  },
});
